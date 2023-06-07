from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from .models import Profile
from .forms import CustomPasswordChangeForm


def register(request):
    """
    This is a view function for user registration that handles form submission and rendering of
    registration templates.

    :param request: The request object represents the HTTP request that the user has made to the server.
    It contains information about the request, such as the HTTP method used (e.g. GET or POST), the URL
    requested, and any data submitted in the request
    :return: If the request method is "POST" and the user registration form is valid, a new user is
    created with the provided information and saved to the database. Then, the "register_done.html"
    template is rendered with the new user object passed as context. If the request method is not
    "POST", the "register.html" template is rendered with an empty user registration form passed as
    context.
    """
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})

    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd["password"])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated Successfully")

                return HttpResponse("Disabled account")

            return HttpResponse("invalid login")

    else:
        form = LoginForm
    return render(request, "account/login.html", {"form": form})


class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/password_change_form.html'


# from django.shortcuts import render
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from .forms import UserRegistrationForm, LoginForm
