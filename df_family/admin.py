from django.contrib import admin
from .models import Family


class FamilyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    pass

admin.site.register(Family, FamilyAdmin)