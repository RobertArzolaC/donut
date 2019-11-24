from django.urls import path
from .views import LoginView, RegisterUsers


urlpatterns = [
    path('login/', LoginView.as_view(), name="auth-login"),
    path('register/', RegisterUsers.as_view(), name="auth-register"),
]
