from django.urls import path

from . import views

urlpatterns = [
    path("shoes", views.ShoesView.as_view()),
    path("shoes/<int:pk>", views.ShoewViewId.as_view()),
]
