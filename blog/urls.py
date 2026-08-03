from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path("",views.BlogMainPageView.as_view(),name='index'),
    path("list/",views.BlogListView.as_view(),name='list'),
    path("dashboard/",views.BlogDashboardView.as_view(),name='dashboard'),
    path("post/<int:pk>/",views.PostDetailView.as_view(),name='post-detail'),
    path("post/<int:pk>/edit/",views.PostUpdateView.as_view(),name='post-edit'),
    path("post/<int:pk>/delete/",views.PostDeleteView.as_view(),name='post-delete'),
    path("post/write/",views.PostCreateView.as_view(),name='post-create'),
]