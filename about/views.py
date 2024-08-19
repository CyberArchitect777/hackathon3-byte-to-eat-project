from django.shortcuts import render
from .models import About, Snack_Profile
from django.views import generic


def about(request):
    about = About.objects.first()
    profile_list = Snack_Profile.objects.all()

    for profile in profile_list:
        print("Image - " + str(profile.image))

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "profile_list": profile_list
        },
    )


class ProfileList(generic.ListView):
    queryset = Snack_Profile.objects.all()
    template_name = "about.html"
