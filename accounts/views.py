from django.utils.http import url_has_allowed_host_and_scheme
from django.shortcuts import render,redirect,resolve_url
from .forms import CustomUserCreationForm,UserForm
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.views import generic
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.views import LoginView
from devgit.services.gitea import create_gitea_user


class SignUpView(generic.CreateView):
    template_name = "auth/signup.html"
    model = CustomUser
    form_class = CustomUserCreationForm

    def form_valid(self, form):

        password = form.cleaned_data["password1"]

        gitea_user = create_gitea_user({"username": form.cleaned_data["username"],"email": form.cleaned_data["email"],"password": form.cleaned_data["password1"],})

        response = super().form_valid(form)

        self.object.gitea_user_id = gitea_user["id"]
        self.object.save(update_fields=["gitea_user_id"])

        login(self.request, self.object)

        return response
    
    def get_success_url(self):
        next_url = (
        self.request.POST.get("next")
        or self.request.GET.get("next")
        )

        if next_url and url_has_allowed_host_and_scheme(
            next_url,
            allowed_hosts={self.request.get_host()},
            require_https=self.request.is_secure(),
        ):
            return next_url

        return resolve_url("core:home")

    
class CustomLoginView(LoginView):
    def form_valid(self, form):
        super().form_valid(form)
        
        messages.success(self.request,f"با موفقیت وارد شدی {self.request.user}") 
        return redirect(self.get_success_url())
    
    def get_success_url(self):
        next_url = (
        self.request.POST.get("next")
        or self.request.GET.get("next")
        )

        if next_url and url_has_allowed_host_and_scheme(
            next_url,
            allowed_hosts={self.request.get_host()},
            require_https=self.request.is_secure(),
        ):
            return next_url

        return resolve_url("core:home")
    
class LogoutView(generic.View):
    
    def get(self,request,*args,**kwargs):
        return render(request,"auth/logout.html")
    
    def post(self,request,*args,**kwargs):
        logout(request)
        messages.success(request,"با موفقیت خارج شدی")
        return redirect("core:home")
    
class ProfileView(generic.DetailView):
    slug_field = "username"
    slug_url_kwarg = "username"
    model = CustomUser
    template_name = "accounts/profile.html"
    context_object_name = "profile"

class ProfileEditView(generic.UpdateView):
    model = CustomUser
    template_name = "accounts/profile-edit.html"
    form_class = UserForm
    
    def get_success_url(self):
        return reverse_lazy(
            "accounts:profile",
            kwargs={"username": self.object.username}
        )

    def get_object(self, queryset = ...):
        print("USER:", self.request.user)
        print("AUTH:", self.request.user.is_authenticated)
        return self.request.user
    
class DashboardView(generic.TemplateView):
    template_name = "accounts/dashboard.html"