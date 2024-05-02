from django.urls import path

from .views import (
    UserRegisterView,
    UserLoginView,
    UserDetailView,
    UserUpdateView,
    UsersListView
)

urlpatterns = [
    path('register', UserRegisterView.as_view()),
    path('login', UserLoginView.as_view()),
    path('user', UserDetailView.as_view()),
    path('list', UsersListView.as_view()),
    # path('delete/', UserDeleteView.as_view()),
    path('update/<int:pk>', UserUpdateView.as_view()),
]