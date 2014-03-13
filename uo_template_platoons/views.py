from django.shortcuts import render, get_object_or_404
from uo_template_platoons.models import Period, Army, Branch
from django.http import HttpResponse

# Create your views here.

def index(request):
  periods = Period.objects.all()
  armies = Army.objects.all()
  branches = Branch.objects.all()
  context = {'periods': periods, 'armies': armies, 'branches': branches }
  return render(request, 'uo_template_platoons/index.html', context)

def period(request, periodname):
  period = get_object_or_404(Period, name=periodname)
  context = {'period': period}
  return render(request, 'uo_template_platoons/period.html', context)

def branch(request, branchname):
  branch = get_object_or_404(Branch, name=branchname)
  context = {'branch': branch}
  return render(request, 'uo_template_platoons/branch.html', context)

def army(request, armyname):
  army = get_object_or_404(Army, name=armyname)
  context = {'army': army}
  return render(request, 'uo_template_platoons/army.html', context)
