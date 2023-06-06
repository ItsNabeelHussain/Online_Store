from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, LoginForm


  
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
            return render(request, 'account/register_done.html', {'new_user': new_user})

    else:
        user_form = UserRegistrationForm()
        return render(request, 'account/register.html', {'user_form': user_form})
