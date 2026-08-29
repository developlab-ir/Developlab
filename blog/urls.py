from django.urls import path
from . import views


app_name = "blog"
    
urlpatterns = [
    path("",views.BlogMainPageView.as_view(),name='index'),
    path("list/",views.BlogListView.as_view(),name='list'),
    path("dashboard/",views.BlogDashboardView.as_view(),name='dashboard'),
    path("post/<int:pk>/",views.PostDetailView.as_view(),name='post-detail'),
    path("post/<int:pk>/comments/write/",views.CommentCreateView.as_view(),name='write-comment'),
    path("post/<int:pk>/comments/<int:comment_id>/delete/",views.CommentDeleteView.as_view(),name='delete-comment'),
    path("post/<int:pk>/edit/",views.PostUpdateView.as_view(),name='post-edit'),
    path("post/<int:pk>/delete/",views.PostDeleteView.as_view(),name='post-delete'),
    path("post/write/",views.PostCreateView.as_view(),name='post-create'),
]