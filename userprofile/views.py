from django.shortcuts import render
from django.contrib.auth.decorators import login_required # Ensures only logged in users will see this page

# Create your views here.

@login_required 
def display_profile(request):
    return render(request,"userprofile/profile.html",)

def review_dashboard(request):
    return render(request, "userprofile/reviewdashboard.html")