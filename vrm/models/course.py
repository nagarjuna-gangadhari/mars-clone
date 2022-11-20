'''
    Course related tables
'''

from tkinter import CASCADE
from django.db import models
# from vrm.models.schedule import Ay
from utils.choicess import *
from django.core.validators import MaxValueValidator, MinValueValidator
from utils.models import Language
import settings


class Role(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    description = models.CharField(max_length=1024, null=True, blank=True)
    type = models.IntegerField(choices=((1,'Internal'), (2,'External')), default=2)
    
    def __str__(self):
        return self.name
    

class Course(models.Model):
    board = models.CharField(max_length=128,choices=BOARD_CHOICESS, null=True, blank=True)
    subject = models.CharField(max_length=128, null=True, blank=True,db_index=True)
    grade = models.IntegerField(default=1, validators=[MaxValueValidator(settings.MAX_GRADE), MinValueValidator(settings.MIN_GRADE)])
    description = models.TextField(max_length=2048, null=True, blank=True)
    picture = models.FileField(upload_to='static/uploads/images/course', null=True, blank=True)
    language = models.ForeignKey(Language, null=True, blank=True)
    availabilityType = models.CharField(max_length=50, choices=(('1', 'Web1.0 Only'), ('2', 'Mobile App only'),('3', 'All Platforms')), default="3")
    status = models.IntegerField(choices=((1,'Active'), (2,'Inactive')), default=1)

    def __str__(self):
        return "%s-%s-%s" % (self.board, self.grade, self.subject)


class Topic(models.Model):
    title = models.CharField(max_length=512)
    course = models.ForeignKey(Course,db_index=True)
    num_sessions = models.IntegerField(default=1)
    status = models.IntegerField(choices=((1,'Active'), (2,'Inactive')), default=1)
    
    def __str__(self):
        return self.title


class SubTopic(models.Model):
    name = models.CharField(max_length=1024, null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=CASCADE)
    status = models.IntegerField(choices=((1,'Active'), (2,'Inactive')), default=1)

    def __str__(self):
        return self.name