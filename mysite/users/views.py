from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate
# Create your views here.

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data("username")
        password = form.cleaned_data("password")

        user = authenticate(username=username, password=password)