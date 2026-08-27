from django.urls import path
from . import views
from .autocomplete import CategoryAutocomplete


app_name = 'core'

urlpatterns = [
    path('',views.MainToHomeView.as_view(),name='main'),
    path('home/',views.HomePageView.as_view(),name='home'),
    path("category-autocomplete/",CategoryAutocomplete.as_view(),name="category-autocomplete"),
]