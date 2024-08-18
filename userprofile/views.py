from django.contrib.auth.decorators import login_required # Ensures only logged in users will see this page
from django.shortcuts import render, redirect # function is a shortcut for rendering a template and returning an HTTP response
from django.contrib import messages # Django's built-in messaging system/feedback to user
from django.urls import reverse_lazy # Handles URL redirection
from index.models import Review # Import Review model
from index.forms import ReviewForm # Import Review form

# Create your views here.

# User profile - sorry, this is the same as the "Add a Review" def down below. I'm not sure which is correct - Tina
#@login_required 
#def add_review(request):
   # return render(
       # request, 
        #"userprofile/review_dashboard.html"
    #)

# User dashboard that shows all their reviews
@login_required 
def review_dashboard(request):

    user_reviews = Review.objects.filter(poster=request.user)

    return render(
        request, 
        "userprofile/review_dashboard.html", {
        "user_reviews": user_reviews
        }
    )


# Add a review
def add_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("review_dashboard") # Redirects User to dashboard with all their reviews
    else:
        form = ReviewForm()
    return render(request, "userprofile/add_review.html", {"form": form})


# Edit a review
@login_required
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
def delete_review(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect("review_dashboard") # Redirects User to dashboard with all their reviews