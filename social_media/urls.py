from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("social", views.SocialMediaView.as_view()),
    path("social/<int:pk>", views.SocialMediaViewId.as_view()),
]
