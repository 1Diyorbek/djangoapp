from django.urls import path
from .views import LandingPageView, BookView, AboutBookView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('book/', BookView.as_view(), name='book'),
    path('about_book/<int:id>', AboutBookView.as_view(), name='about_book'),
]
