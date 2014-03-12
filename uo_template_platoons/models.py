from django.db import models

# Create your models here.

class Period(models.Model):
  name = models.CharField(max_length = 1024)
  description = models.TextField()
  start = models.DateField()

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

class Branch(models.Model):
  name = models.CharField(max_length=1024)
  description = models.TextField()

class Platoon(models.Model):
  title = models.CharField(max_length=1024)
  description = models.TextField()
  army = models.ForeignKey('Army')
  branch = models.ForeignKey('Branch')
  period = models.ForeignKey('Period')

class Section(models.Model):
  name = models.CharField(max_length=1024)
  description = models.TextField()
  platoon = models.ForeignKey('Platoon')

class Unit(models.Model):
  name = models.CharField(max_length=1024)
  description = models.TextField()
  section = models.ForeignKey('Section')



