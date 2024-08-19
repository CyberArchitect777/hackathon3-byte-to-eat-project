from django.core.exceptions import PermissionDenied # If a user tries to do something they don't have permission for = 403 Forbidden response
from django.shortcuts import get_object_or_404
from index.models import Review
from functools import wraps

def require_superuser(view_func): # Checks if user is superuser
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied("You have no power here! Permission denied.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def require_review_ownership(view_func): # Checks if user that is trying to access a specific review is actually the owner (or a superuser)
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        review_id = kwargs.get("pk")
        review = get_object_or_404(Review, pk=review_id)

        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)

        if review.poster != request.user:
            raise PermissionDenied("You do not have permission to edit or delete this review.")

        return view_func(request, *args, **kwargs)
    return _wrapped_view