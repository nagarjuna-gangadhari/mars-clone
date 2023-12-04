from django.contrib import admin

from .models.base import *
from django.apps import apps


# class ListAdminMixin(object):
#     def __init__(self, model, admin_site):
#         self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
#         super(ListAdminMixin, self).__init__(model, admin_site)

# for m in [your_model_name]:
#     mod = getattr(models, m)
#     admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
#     try:
#         admin.site.register(mod, admin_class)
#     except admin.sites.AlreadyRegistered:
#         pass




for model in apps.get_app_config('assessments').models.values():
    admin.site.register(model)