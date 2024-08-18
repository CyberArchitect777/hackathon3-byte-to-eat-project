from django.contrib.auth.mixins import UserPassesTestMixin # If user fails test they are denied access
from django.core.exceptions import PermissionDenied # If a user tries to do something they don't have permission for = 403 Forbidden response

"""
If an unauthorized user tries to access a review that they are not the
owner of (or not a superuser/admin), access will be denied and they will
diverted elsewhere.
"""

class RequireSuperuserMixin(UserPassesTestMixin): # Checks if user is superuser
    def is_superuser(self):
        return self.request.user.is_superuser

    def redirect_if_not_superuser(self): # If user is not superuser, user gets redirected to the login page
        return self.redirect_to_login()


class RequireReviewOwnershipMixin: # Checks if user that is trying to access a specific review is actually the owner
    def validate_review_access(self, request, *args, **kwargs):
        review = self.get_review_object()

        # Allows superusers to access any review even if they are not the owner
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        # Ensures that only the owner can access the review
        if review.user != request.user: # Or is it review.poster? test and check
            raise PermissionDenied("You do not have permission to edit or delete this review.")

        return super().dispatch(request, *args, **kwargs)

    def get_review_object(self):
        return self.get_object()  # Retrieves the review object related to the current request
