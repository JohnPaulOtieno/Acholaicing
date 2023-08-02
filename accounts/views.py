from django.views.generic.base import TemplateView
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from .forms import SignUpForm
from django.shortcuts import render

class LoginView(TemplateView):
    template_name = "accounts/login.html"

    def post(self, request):

        if request.user.is_authenticated:
            return redirect('homepage')

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('homepage')
        else:
            messages.success(request, 'There was an error logging you in.')
            return redirect('login')

class RegisterView(View):
    template_name = "accounts/register.html"

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # auth and log in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered. Welcome.')
            return redirect('homepage')
        else:
            messages.success(request, 'There was an error registering you. ')
            return redirect('register')
    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

class LogoutUser(View):

    def get(self, request):
        logout(request)
        messages.success(request, 'You Have Been Logged Out...')
        return redirect('login')