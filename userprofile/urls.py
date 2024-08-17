from django.urls import path
from . import views

urlpatterns = [
    path("", views.display_profile, name="display_profile"),

    # User dashboard page where they can see all their review
    path("review_dashboard/", views.review_dashboard, name="review_dashboard"),

    # So User can add a new review
    path("add_review/", views.add-review, name="add_review"),

     # So User can edit their existing review
    path("edit_review/<pk>/", views.edit-review, name="edit_review"),

     # So User can delete their existing review
    path("delete_review/<pk>/", views.delete-review, name="delete_review"),
]