from django.shortcuts import render, get_object_or_404
from uo_template_platoons.models import Period
from django.http import HttpResponse

# Create your views here.

def index(request):
  periods = Period.objects.all()
  context = {'periods': periods}
  return render(request, 'uo_template_platoons/index.html', context)

def period(request, periodname):
  period = get_object_or_404(Period, name=periodname)
  context = {'period': period}
  return render(request, 'uo_template_platoons/period.html', context)
