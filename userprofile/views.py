from django.shortcuts import render
from django.contrib.auth.decorators import login_required # Ensures only logged in users will see this page

# Create your views here.

# User profile
@login_required 
def display_profile(request):
    return render(request,"userprofile/profile.html",)

# User dashboard that shows all their reviews
def review_dashboard(request):
    return render(request, "userprofile/reviewdashboard.html")


# Add a review
def add_review(request):
    if request.method = "POST":
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
    if request.method = "POST":
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

