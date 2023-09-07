from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in
            return redirect('Articlelist')
    else:
        form = UserCreationForm()
    return render(request, 'Authentication/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log in the user
            return redirect('Articlelist')
            
            # if 'next' in request.POST:
                # return redirect(request.POST.get('next'))
        else:
            return HttpResponse('error email or pw')
    else:
        form = AuthenticationForm()
    return render(request, 'Authentication/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
