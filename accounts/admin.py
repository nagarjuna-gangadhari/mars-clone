from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class UserAdmin(UserAdmin):
    model = User



admin.site.register(User, UserAdmin)
admin.site.register(Profile, admin.ModelAdmin)
admin.site.register(Location, admin.ModelAdmin)
admin.site.register(Role, admin.ModelAdmin)
admin.site.register(UserRoleMaping, admin.ModelAdmin)
admin.site.register(UserRoleMeeting, admin.ModelAdmin)

