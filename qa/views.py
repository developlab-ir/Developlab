from django.views import generic
from .models import Question,Answer
from .forms import QuestionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy


class QuestionListView(generic.ListView):
    template_name = "questions/question-list.html"
    model = Question
    context_object_name = "questions"
    
    def get_queryset(self):
            return Question.objects.filter(is_active=True).order_by("is_pin","-write_date","-solved")

class QuestionDetailView(generic.DetailView):
    template_name = "questions/question-detail.html"
    model = Question
    pk_url_kwarg = "pk"
    context_object_name = "question"

    def get_queryset(self):
            query = Question.objects.filter(id=self.kwargs.get(self.pk_url_kwarg),is_active=True)
            return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["answers"] = self.object.answers.all()
        return context

class QuestionCreateView(LoginRequiredMixin,generic.CreateView):
      template_name = "questions/question-write.html"
      model = Question
      form_class = QuestionForm

      def get_success_url(self):
            return super().get_success_url()

      def form_valid(self, form):
              form.instance.user = self.request.user
              return super().form_valid(form)

class QuestionUpdateView(LoginRequiredMixin,generic.UpdateView):
    template_name = "questions/question-edit.html"
    model = Question
    form_class = QuestionForm

    def dispatch(self, request, *args, **kwargs):
        query = Question.objects.filter(id=self.kwargs.get(self.pk_url_kwarg),user=request.user)
        if not query.exists():
            messages.error(request,"شما نویسنده ی این سوال نیستید")
            return redirect(self.success_url)
        if query.filter(is_active=False):
            messages.error(request,"این سوال در دسترس نیست")
            return redirect(self.success_url)

        return super().dispatch(request, *args, **kwargs)

class QuestionDeleteView(LoginRequiredMixin,generic.DeleteView):
    template_name = "questions/question-delete.html"
    model = Question
    success_url = reverse_lazy("qa:question-list")

    def dispatch(self, request, *args, **kwargs):
        query = Question.objects.filter(id=self.kwargs.get(self.pk_url_kwarg),user=request.user)
        if not query.exists():
            messages.error(request,"شما نویسنده ی این سوال نیستید")
            return redirect(self.success_url)
        if query.filter(is_active=False):
            messages.error(request,"این سوال در دسترس نیست")
            return redirect(self.success_url)

        return super().dispatch(request, *args, **kwargs)

class AnswerCreateView(LoginRequiredMixin,generic.View):
    def post(self, request, pk):
            question = get_object_or_404(Question, pk=pk)
            description = request.POST.get("description")
    
            if not description:
                messages.error(request, "متن پاسخ نباید خالی باشد.")
                return redirect(question.get_absolute_url())
            Answer.objects.create(
                question=question,
                user=request.user,
                description=description,
            )
    
            messages.success(request, "پاسخ شما ثبت شد.")
            return redirect(question.get_absolute_url())