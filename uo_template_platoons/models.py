from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy

# Create your models here.

class Period(models.Model):
  name = models.CharField(max_length=1024, unique=True)
  description = models.TextField()
  start = models.DateField()
  owner = models.ForeignKey(User)
  
  def get_absolute_url(self):
    return reverse_lazy('uo_template_platoons.views.period', args=[self.name])

  def __str__(self):
    return self.name

class Army(models.Model):
  WEST = 'W'
  EAST = 'E'
  THIRD = 'O'
  SIDE_CHOICES = (
      (WEST, 'West / BLUFOR'),
      (EAST, 'East / REDFOR'),
      (THIRD, 'Third World / Independent Forces / INDFOR')
      )
  side = models.CharField(max_length=1, choices=SIDE_CHOICES, default=WEST)
  name = models.CharField(max_length=1024)
  owner = models.ForeignKey(User)

  class Meta:
    verbose_name_plural = 'armies'

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse_lazy('uo_template_platoons.views.army', args=[self.name])

class Branch(models.Model):
  name = models.CharField(max_length=1024, unique=True)
  description = models.TextField()
  owner = models.ForeignKey(User)

  class Meta:
    verbose_name_plural = 'branches'

  def get_absolute_url(self):
    return reverse_lazy('uo_template_platoons.views.branch', args=[self.name])

  def __str__(self):
    return self.name

class Platoon(models.Model):
  title = models.CharField(max_length=1024)
  description = models.TextField()
  army = models.ForeignKey(Army)
  branch = models.ForeignKey(Branch)
  period = models.ForeignKey(Period)
  owner = models.ForeignKey(User)
  sections = models.ManyToManyField('Section', through='SectionDeployment')

  def __str__(self):
    return self.title

class SectionDeployment(models.Model):
  section = models.ForeignKey('Section')
  platoon = models.ForeignKey(Platoon)
  count = models.IntegerField()

class Section(models.Model):
  name = models.CharField(max_length=1024)
  description = models.TextField()
  units = models.ManyToManyField('Unit', through='UnitDeployment')

  def __str__(self):
    return self.name

class UnitDeployment(models.Model):
  unit = models.ForeignKey('Unit')
  section = models.ForeignKey(Section)
  count = models.IntegerField()

class Unit(models.Model):
  name = models.CharField(max_length=1024)
  description = models.TextField()

  def __str__(self):
    return self.name
