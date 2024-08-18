from django.shortcuts import render
from .models import About


def about(request):
    about = About.objects.first()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
        },
    )
