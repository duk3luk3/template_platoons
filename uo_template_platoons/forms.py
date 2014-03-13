from django.forms import ModelForm
from uo_template_platoons.models import Period, Army, Branch, Platoon, Section, Unit

class PeriodForm(ModelForm):
  class Meta:
    model = Period
    fields = ['name','description', 'start']

class ArmyForm(ModelForm):
  class Meta:
    model = Army
    fields = ['side','name']

class BranchForm(ModelForm):
  class Meta:
    model = Branch
    fields = ['name','description']

class PlatoonForm(ModelForm):
  class Meta:
    model = Platoon
    fields = ['title','description','army', 'branch','period']

class SectionForm(ModelForm):
  class Meta:
    model = Section
    fields = ['name','description']

class UnitForm(ModelForm):
  class Meta:
    model = Section
    fields = ['name','description']
