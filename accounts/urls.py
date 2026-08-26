from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from django.urls import reverse_lazy
from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path("signup/",views.SignUpView.as_view(),name="signup"),
    path("login/",views.CustomLoginView.as_view(template_name="auth/login.html"),name="login"),
    path("logout/",views.LogoutView.as_view(),name="logout"),
    path("change_password/",PasswordChangeView.as_view(template_name="auth/password-change.html",success_url = reverse_lazy("accounts:password_change_done")),name="password_change"),
    path("change_password/done/",PasswordChangeDoneView.as_view(template_name="auth/password-change-done.html"),name="password_change_done"),

    path("profile/edit/",views.ProfileEditView.as_view(),name="profile-edit"),
    path("profile/<str:username>/",views.ProfileView.as_view(),name="profile"),
    path("dashboard/",views.DashboardView.as_view(),name="dashboard"),
]