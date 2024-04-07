from django.urls import path
from .views import StudentRegisterView, StudentLoginView


urlpatterns = [
    path("register/", StudentRegisterView.as_view(), name='register'),
    path("login/", StudentLoginView.as_view(), name='login')
]