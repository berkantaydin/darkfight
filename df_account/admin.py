from django.contrib import admin
from .models import UserProfile, UserProperties


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserProfileAdmin)


class UserPropertiesAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProperties, UserPropertiesAdmin)


