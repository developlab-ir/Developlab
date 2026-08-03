from django.views import generic
from django.urls import reverse_lazy
from django.conf import settings
from django.shortcuts import redirect
from django.utils.translation import activate


class MainToHomeView(generic.RedirectView):
    url = reverse_lazy("core:home")

class HomePageView(generic.TemplateView):
    template_name = "core/index.html"
