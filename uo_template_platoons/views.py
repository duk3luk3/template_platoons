from django.shortcuts import render, get_object_or_404, redirect
from uo_template_platoons.models import Period, Army, Branch
from uo_template_platoons.forms import PeriodForm, ArmyForm, BranchForm, SectionForm, UnitForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class OwnedCreateView(CreateView):
  template_name_suffix='_create_form'

  def form_valid(self, form):
    obj = form.save(commit=False)
    obj.owner = self.request.user
    obj.save()
    return HttpResponseRedirect(obj.get_absolute_url())

class OwnedEditView(UpdateView):
  template_name_suffix = '_create_form'

  def dispatch(self, request, *args, **kwargs):
    obj = get_object_or_404(self.model, pk=kwargs['pk'])
    if not obj.owner == request.user:
      return HttpResponse("You are not the owner of that object.")
    else:
      return super(OwnedEditView, self).dispatch(request, *args, **kwargs)

class OwnedDeleteView(DeleteView):
  success_url = reverse_lazy('index')

  def dispatch(self, request, *args, **kwargs):
    obj = get_object_or_404(self.model, pk=kwargs['pk'])
    if not obj.owner == request.user:
      return HttpResponse("You are not the owner of that object.")
    else:
      return super(OwnedDeleteView, self).dispatch(request, *args, **kwargs)

class PeriodCreateView(OwnedCreateView):
  model = Period
  fields = ['name', 'description', 'start']

class PeriodEditView(OwnedEditView):
  model = Period
  fields = ['name', 'description', 'start']

class PeriodDeleteView(OwnedDeleteView):
  model = Period

class BranchCreateView(OwnedCreateView):
  model = Branch
  fields = ['name', 'description']

class BranchEditView(OwnedEditView):
  model = Branch
  fields = ['name', 'description']

class BranchDeleteView(OwnedDeleteView):
  model = Branch

class ArmyCreateView(OwnedCreateView):
  model = Army
  fields = ['name', 'side']

class ArmyEditView(OwnedEditView):
  model = Army
  fields = ['name', 'side']

class ArmyDeleteView(OwnedDeleteView):
  model = Army


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

def period_edit(request, periodname=None):
  if not request.user.is_authenticated():
    return HttpResponse("Sorry, only authenticated users can edit stuff.")

  if request.method == 'POST':
    form = PeriodForm(request.POST)
    if form.is_valid():
      m = form.save(commit=False)
      m.owner = request.user
      m.save()
      return redirect('uo_template_platoons.views.period_view', periodname=m.name)
  else:
    try:
      period = Period.objects.get(name=periodname)
      form = PeriodForm(instance=period)
    except:
      period = None
      form = PeriodForm()

    if period is not None and request.user != period.owner:
      return HttpResponse("Sorry, you can only edit things you own.")


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
