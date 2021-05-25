from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import MalRequirements

"""Subclassing CreateView."""


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # use reverse_lazy since load urls when available
    template_name = 'registration/signup.html'


def mal_Requirements(request):
    mal = MalRequirements.objects.all()

    return render(request, "user_page.html", {"mal": mal})
