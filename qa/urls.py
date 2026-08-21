from django.urls import path
from . import views


app_name = "question"

urlpatterns = [
    path("list/",views.QuestionListView.as_view(),name="question-list"),
]