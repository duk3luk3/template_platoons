from django.contrib import admin
from uo_template_platoons.models import Platoon, Army, Branch, Section, Unit, Period


# Register your models here.

class SectionInline(admin.StackedInline):
  model = Section
  extra = 3

class PlatoonAdmin(admin.ModelAdmin):
  inlines = [SectionInline]

admin.site.register(Platoon, PlatoonAdmin)
admin.site.register(Army)
admin.site.register(Branch)
admin.site.register(Period)
