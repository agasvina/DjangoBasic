from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/")
        # print("Is login?", request.user.is_authenticated())

    return render(request, "accounts/form.html", {"form": form})

def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        #This is built in method for user model
        user.set_password(password)
        user.save()

        #Try the user to login in.
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        new_user = authenticate(username=username, password=password)
        login(request, new_user)
        return redirect("/")


    return render(request, "accounts/form.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("/")

