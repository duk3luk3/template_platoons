from django.shortcuts import render, get_object_or_404, redirect
from uo_template_platoons.models import Period, Army, Branch, Platoon, Section, Unit, SectionDeployment, UnitDeployment
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
  platoons = Platoon.objects.all()
  context = {'periods': periods, 'armies': armies, 'branches': branches, 'platoons': platoons }
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

def platoon(request, platoonname):
  platoon = get_object_or_404(Platoon, title=platoonname)
  sectiondeployments = SectionDeployment.objects.filter(platoon=platoon).all()

  ud = lambda s: [{'count':ud.count, 'name':ud.unit.name,'description':ud.unit.description} for ud in UnitDeployment.objects.filter(section=s).all()]

  sections = [{'count':sd.count,'name':sd.section.name,'description':sd.section.description,'units':ud(sd.section)} for sd in sectiondeployments]

  context = {'platoon':platoon, 'sections':sections}

  return render(request, 'uo_template_platoons/platoon.html', context)


