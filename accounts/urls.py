from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path("signup/",views.SignUpView.as_view(),name="signup"),
    path("login/",views.CustomLoginView.as_view(template_name="auth/login.html"),name="login"),
    path("logout/",views.LogoutView.as_view(),name="logout"),
    path("profile/edit/",views.ProfileEditView.as_view(),name="profile-edit"),
    path("profile/<str:username>/",views.ProfileView.as_view(),name="profile"),
    path("dashboard/",views.DashboardView.as_view(),name="dashboard"),
]