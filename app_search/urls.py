from django.urls import path

from .views import UniversalSearchView

urlpatterns = [
    path('', UniversalSearchView.as_view()),
]
