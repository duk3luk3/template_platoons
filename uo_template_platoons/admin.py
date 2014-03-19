from django.contrib import admin
from uo_template_platoons.models import Platoon, Army, Branch, Section, Unit, Period, SectionDeployment, UnitDeployment


# Register your models here.

class SectionInline(admin.StackedInline):
  model = Platoon.sections.through
  extra = 3

class PlatoonAdmin(admin.ModelAdmin):
  inlines = [SectionInline]

class UnitInline(admin.TabularInline):
  model = Section.units.through
  extra = 3

class SectionAdmin(admin.ModelAdmin):
  inlines = [UnitInline]

admin.site.register(Platoon, PlatoonAdmin)
admin.site.register(Army)
admin.site.register(Branch)
admin.site.register(Period)
admin.site.register(Section, SectionAdmin)
admin.site.register(Unit)
admin.site.register(SectionDeployment)
admin.site.register(UnitDeployment)
