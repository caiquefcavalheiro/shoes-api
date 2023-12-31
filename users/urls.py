from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("users", views.CreateUserView.as_view()),
    path("users", views.ListUserView.as_view()),
    path("users/<int:pk>", views.UserDetailView.as_view()),
    path("login", TokenObtainPairView.as_view()),
]
