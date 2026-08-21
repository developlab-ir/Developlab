from django.views import generic
from .models import Question,Answer


class QuestionListView(generic.ListView):
    template_name = "questions/question-list.html"
    model = Question
    context_object_name = "questions"
    
    def get_queryset(self):
            return Question.objects.filter(is_active=True).order_by("is_pin","-write_date","-solved")
