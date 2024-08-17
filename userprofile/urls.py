from django.urls import path
from . import views

urlpatterns = [
    path("review-dashboard/", views.review_dashboard, name="review_dashboard"),
]