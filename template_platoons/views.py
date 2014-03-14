from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from template_platoons.forms import LoginForm
from django.template import RequestContext

# Create your views here.

def index(request):

  context = {'content': 'This is the site index.'}
  return render(request, 'index.html', context)

def user(request,username):
  try:
    u = User.objects.get(username=username)
    return HttpResponse('Hello. This is %s\'s user profile.' % (username))
  except User.DoesNotExist:
    return HttpResponse('There is no user called %s!' % (username))

def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(username=username, password=password)

      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponse("Welcome, %s" % (username))
        else:
          return HttpResponse("Sorry, your user account is disabled.")

  else:
    form = LoginForm()

  context = { 'form': form }

  return render(request, 'login.html', context)

def logout_view(request):
  logout(request)

  return index(request)
