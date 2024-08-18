from django.urls import path
from . import views

urlpatterns = [
    # path("", views.review_dashboard, name="review_dashboard"),

    # User dashboard page where they can see all their review
    path("review_dashboard/", views.review_dashboard, name="review_dashboard"),

    # So User can add a new review
    path("add_review/", views.add_review, name="add_review"),

     # So User can edit their existing review
    path("edit_review/<int:pk>/", views.edit_review, name="edit_review"),

     # So User can delete their existing review
    path("delete_review/<int:pk>/", views.delete_review, name="delete_review"),
]