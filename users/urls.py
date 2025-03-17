
from django.urls import path, include
from .views import RegisterView, LoginView, UserView, LoggoutView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LoggoutView.as_view())
]