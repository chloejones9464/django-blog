from django.shortcuts import render, get_object_or_404
from .models import About

# Create your views here.

queryset = About.objects.all().order_by('-update_on').first()


def about_me(request, about):
    return render(
        request,
        "about/about.html",
        {"about": about},
    )




