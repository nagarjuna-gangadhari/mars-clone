from django.db import models
from accounts.models import User

class BaseModel(models.Model):
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_created_by')
    updated_by = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_updated_by')
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
        

class Location(models.Model):
    country_id = models.IntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=20, null=True, blank=True)
    country_name = models.CharField(max_length=128, null=True, blank=True)
    state_name = models.CharField(max_length=128, null=True, blank=True)
    city_name = models.CharField(max_length=128, null=True, blank=True)
    
    def __str__(self):
        return self.city_name
    
class Language(models.Model):
    name = models.CharField(max_length=256, null=False)
    code = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name
