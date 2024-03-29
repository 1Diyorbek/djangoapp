from django.urls import path
from .views import greeting, image

urlpatterns = [
    path('greeting/', greeting),
    path('image/', image),
]
