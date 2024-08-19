from django.shortcuts import render
from .models import About, Snack_Profile
from django.views import generic
from django.views.generic import TemplateView, ListView # star ratings instead of numbers


def about(request):
    about = About.objects.first()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
        },
    )


class ProfileList(generic.ListView):
    queryset = Snack_Profile.objects.all()
    template_name = "about.html"
