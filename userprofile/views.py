from django.shortcuts import render
from django.contrib.auth.decorators import login_required # Ensures only logged in users will see this page
from index.models import Review

# Create your views here.

# User profile
@login_required 
def add_review(request):
    return render(
        request, 
        "userprofile/addareview.html"
    )

@login_required 
def review_dashboard(request):

    user_reviews = Review.objects.filter(poster=request.user)

    return render(
        request, 
        "userprofile/reviewdashboard.html", {
        "user_reviews": user_reviews
        }
    )
