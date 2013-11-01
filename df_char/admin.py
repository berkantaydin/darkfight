from django.contrib import admin
from .models import FirstName, LastName


class FirstNameAdmin(admin.ModelAdmin):
    list_display = ('name',)
    pass

admin.site.register(FirstName, FirstNameAdmin)


class LastNameAdmin(admin.ModelAdmin):
    list_display = ('name',)
    pass

admin.site.register(LastName, LastNameAdmin)