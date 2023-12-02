from django.db import models
from .choicess import BOARD_CHOICESS


class BaseModel(models.Model):

    created_by = models.ForeignKey('accounts.User', null=True, blank=True, related_name='%(class)s_created_by', on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey('accounts.User', null=True, blank=True, related_name='%(class)s_updated_by', on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
        

class Location(BaseModel):

    country = models.CharField(max_length=128, null=False, blank=False)
    state   = models.CharField(max_length=128, null=False, blank=False)
    city    = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return str(self.pk)
    
class Language(BaseModel):

    name = models.CharField(max_length=256, null=False)
    code = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.name

class Ay(BaseModel):

    name        = models.CharField(max_length=512)
    board       = models.CharField(max_length=128, choices=BOARD_CHOICESS, null=True, blank=True)
    start_date  = models.DateTimeField(null=True, blank=True)
    end_date    =  models.DateTimeField(null=True, blank=True)
    active      = models.BooleanField(default=True)
    
    def __str__(self):
        return  str(self.pk)


class Course(BaseModel):

    board       = models.CharField(max_length=128, null=True, blank=True)
    subject     = models.CharField(max_length=128, null=True, blank=True)
    grade       = models.CharField(max_length=128, null=True, blank=True)
    description = models.CharField(max_length=1024, null=True, blank=True)
    language    = models.ForeignKey(Language, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='language_course')
    active      = models.BooleanField(default=True)

    def __str__(self):
        return str(self.pk)


class Topic(BaseModel):

    name        = models.CharField(max_length=512, null=True, blank=True)
    course      = models.ForeignKey(Course, on_delete=models.DO_NOTHING, related_name='course_topic')
    url         = models.CharField(max_length=1024, null=True, blank=True)
    active      = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.pk)
    

class SubTopic(BaseModel):

    name        = models.CharField(max_length=512, null=True, blank=True)
    topic       = models.ForeignKey(Topic, null=True, blank=True, related_name='course_topic_subtopic', on_delete=models.DO_NOTHING)
    active      = models.BooleanField(default=True)

    def __str__(self):
        return str(self.pk)