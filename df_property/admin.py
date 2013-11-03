from django.contrib import admin
from df_property.models import Property


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'race', 'req_level',)
    pass


admin.site.register(Property, PropertyAdmin)