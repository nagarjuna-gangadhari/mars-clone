from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# class UserAdmin(UserAdmin):
#     model = User

class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ['id', 'country', 'state', 'city']

class NotificationPreferenceAdmin(admin.ModelAdmin):
    model = NotificationPreference
    list_display = [field.name for field in NotificationPreference._meta.get_fields()]

admin.site.register(User, UserAdmin)
admin.site.register(Profile, admin.ModelAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Role, admin.ModelAdmin)
admin.site.register(UserRoleMaping, admin.ModelAdmin)
admin.site.register(UserRoleMeeting, admin.ModelAdmin)
admin.site.register(NotificationPreference, NotificationPreferenceAdmin)

