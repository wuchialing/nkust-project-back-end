from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.contrib import auth

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('trip')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/trip')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/trip")
    else:
        return render(request, 'login.html', locals())
    
def main_page(request):
    return render(request, 'main_page.html')

def log_out(request):
    auth.logout(request)
    return HttpResponseRedirect('/main_page')

# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_my_profile(request):
#     user = request.user
#     return Response({
#         "username": user.username,
#         "email": user.email,
#         "is_staff": user.is_staff,
#         "groups": [g.name for g in user.groups.all()],
#     })
