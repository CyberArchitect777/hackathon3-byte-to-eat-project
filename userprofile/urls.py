from django.urls import path
from . import views

urlpatterns = [
    path("", views.review_dashboard, name="review_dashboard"),
]