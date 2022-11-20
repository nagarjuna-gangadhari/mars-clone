from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.views.generic import View
import json
from django.http import JsonResponse

from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class LoginPageView(View):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        username=request.POST.get('username', None)
        password=request.POST.get('password', None)
        next = request.POST.get('next', None)
        
        print(request.GET)
        
        try:
            if username and password and isinstance(int(username), int):
                user = authenticate(
                    username=username,
                    password=password
                )
                if user is not None:
                    login(request, user)
                    if next: redirect(next)
                    return redirect('/')
        except Exception as e: pass
        message = 'Invalid User Id or Password'
        return render(request, self.template_name, context={'message': message})
    
    
def logout_view(request):
    logout(request)
    return redirect('/')
        
