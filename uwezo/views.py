from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout, auth_login
from django.contrib import messages
def index(request):
    login_form = AuthenticationForm()
    signup_form = UserCreationForm()

    # Handle login form submission
    if 'login' in request.POST:
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = authenticate(
                username=login_form.cleaned_data.get('username'),
                password=login_form.cleaned_data.get('password')
            )
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')  # Success message
                return redirect('dashboard')  # Redirect to dashboard after login
            else:
                messages.error(request, 'No user found with this username or incorrect password.')  # Incorrect username or password
        else:
            messages.error(request, 'Invalid username or password.')  # General form error

    # Handle signup form submission
    elif 'signup' in request.POST:
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            messages.success(request, 'Sign up successful! You are now logged in.')  # Sign up success message
            return redirect('dashboard')  # Redirect to dashboard after sign-up
        else:
            messages.error(request, 'Invalid signup details.')  # General signup error

    return render(request, 'index.html', {
        'login_form': login_form,
        'signup_form': signup_form,
    })

def logout_view(request):
    messages.get_messages(request).used = True  # Clear previous messages
    auth_logout(request)
    messages.success(request, 'Sad to see you go!')
    return redirect('index')

def dashboard(request):
    user = request.user  # Get the currently logged-in user
    if not user.is_authenticated:
        return redirect('index') 
    print(f"User: {user.username}")
    return render(request, 'dashboard.html', {
        'user': user,  # Pass the user object to the template
    })




# other stuff
from .forms import ReportForm

def map(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_list')  # Redirect to a list of reports
    else:
        form = ReportForm()
    return render(request, 'result.html', {'form': form})
def map_view(request):
    return render(request, 'maps.html')