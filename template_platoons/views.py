from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

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
