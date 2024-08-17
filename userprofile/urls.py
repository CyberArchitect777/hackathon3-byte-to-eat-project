from django.urls import path
from . import views

urlpatterns = [
    path("", views.display_profile, name="display_profile"),
    path("review-dashboard/", views.review_dashboard, name="review_dashboard"),
]