from django.urls import path
from . import views


app_name = "qa"

urlpatterns = [
    path("list/",views.QuestionListView.as_view(),name="question-list"),
    path("question/ask/",views.QuestionCreateView.as_view(),name="question-create"),
    path("question/<int:pk>/",views.QuestionDetailView.as_view(),name="question-detail"),
    path("question/<int:pk>/edit",views.QuestionUpdateView.as_view(),name="question-update"),
]