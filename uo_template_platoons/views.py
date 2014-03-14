from django.shortcuts import render, get_object_or_404
from uo_template_platoons.models import Period, Army, Branch
from uo_template_platoons.forms import PeriodForm, ArmyForm, BranchForm, SectionForm, UnitForm
from django.http import HttpResponse

# Create your views here.

def index(request):
  periods = Period.objects.all()
  armies = Army.objects.all()
  branches = Branch.objects.all()
  context = {'periods': periods, 'armies': armies, 'branches': branches }
  return render(request, 'uo_template_platoons/index.html', context)

def period_view(request, periodname):
  period = get_object_or_404(Period, name=periodname)
  context = {'period': period}
  return render(request, 'uo_template_platoons/period.html', context)

def period_edit(request, periodname=None):
  if not request.user.is_authenticated():
    return HttpResponse("Sorry, only authenticated users can edit stuff.")

  if request.method == 'POST':
    form = PeriodForm(request.POST)
    if form.is_valid():
      m = form.save(commit=False)
      m.owner = request.user
      m.save()
      return period_view(request, m.periodname)
  else:
    try:
      period = Period.objects.get(name=periodname)
    except:
      period = None

    if period is not None and request.user != period.owner:
      return HttpResponse("Sorry, you can only edit things you own.")

    form = PeriodForm(period)

  context = {'form': form}

  return render(request, 'uo_template_platoons/edit_period.html', context)



def branch(request, branchname):
  branch = get_object_or_404(Branch, name=branchname)
  context = {'branch': branch}
  return render(request, 'uo_template_platoons/branch.html', context)

def army(request, armyname):
  army = get_object_or_404(Army, name=armyname)
  context = {'army': army}
  return render(request, 'uo_template_platoons/army.html', context)
