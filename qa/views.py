from django.views import generic
from .models import Question,Answer
from .forms import QuestionForm


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

class QuestionCreateView(generic.CreateView):
      template_name = "questions/question-write.html"
      model = Question
      form_class = QuestionForm

      def get_success_url(self):
            return super().get_success_url()

      def form_valid(self, form):
              form.instance.user = self.request.user
              return super().form_valid(form)