from django.contrib.auth.decorators import login_required # Ensures only logged in users will see this page
from django.shortcuts import render, redirect, get_object_or_404, reverse # function is a shortcut for rendering a template and returning an HTTP response
from django.contrib import messages # Django's built-in messaging system/feedback to user
from django.urls import reverse_lazy # Handles URL redirection
from index.models import Review # Import Review model
from index.forms import ReviewForm # Import Review form
from .decorators import require_review_ownership, require_superuser # Import decorators that check for authorized users
from django.views.generic import TemplateView # star ratings instead of numbers

# Create your views here.


# User dashboard that shows all their reviews
@login_required
def review_dashboard(request):

    sort_by = request.GET.get("sort_by", "created_on") # Default sort by date review is created on
    sort_order = request.GET.get("sort_order", "asc") # Default sort order is ascending
    
    if sort_order == "desc": # If sort order is descending
            sort_by = f'-{sort_by}'

    user_reviews = Review.objects.filter(poster=request.user).order_by(sort_by) # Filters reviews so current user can only see their own
        
    return render(
        request, 
        "userprofile/review_dashboard.html", {
        "user_reviews": user_reviews,
        }
    )

# Add a review
@login_required
def add_review(request, review_id=None):
    # Checks that a valid user is logged in. If they're not, user will get message and be redirected to login page
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, "You need to be logged in to add a review.")
        return redirect(reverse("account_login"))

    if review_id: # Checks to see if review_id is provided - this means it's checking if that review already exists and will populate it with data from that review
        review = get_object_or_404(Review, id=review_id) # If there is a review_id, then the form will populate with data from that existing review
    else:
        review = None # If there is no review_id, then the form will be blank/new and ready to be filled in

    # This block handles the form submission
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid(): # Checks if form's validation rules are met
            review = form.save(commit=False) # Doesn't commit form to the database yet
            review.poster = request.user # Assigns the logged-in user to the review
            review.save() # Now saves form to the database
            messages.add_message(request, messages.SUCCESS, "Review successfully added.")
            return redirect("review_dashboard") # Redirects User to dashboard with all their reviews

    # This block handles the GET requests and displays the form
    else:
        form = ReviewForm(instance=review) # Empty form for user to fill in       

    # This block renders the form template
    return render(
        request,
        "userprofile/add_review.html",
        {"form": form, "review": review}
    )


# Edit a review
@login_required
@require_review_ownership
def edit_review(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review.save()
        return redirect("review_dashboard") # Redirects User to dashboard with all their reviews
    else: 
        form = ReviewForm(instance=review)
    return render(request,"userprofile/edit_review.html", {"form": form, "review": review})


# Delete a review
@login_required
@require_review_ownership
def delete_review(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review.delete()
        return redirect("review_dashboard") # Redirects User to dashboard with all their reviews
    return render(request, "delete_reivew.html", {"object": review})