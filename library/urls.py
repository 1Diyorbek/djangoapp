from django.urls import path
from .views import home, after_home

urlpatterns = [
    path('home/', home),
    path('homeafter/', after_home),
]
