from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('',views.MainToHomeView.as_view(),name='main'),
    path('home/',views.HomePageView.as_view(),name='home'),
]