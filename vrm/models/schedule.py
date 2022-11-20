'''
    Time tables models for classes
'''
from tkinter import CASCADE
from django.db import models
from utils.models import BaseModel
from utils.choicess import BOARD_CHOICESS
from vrm.models.center import Center
from vrm.models.course import Course, Topic, SubTopic
from accounts.models import User



class Ay(BaseModel):
    title = models.CharField(max_length=512)
    board = models.CharField(max_length=128, choices=BOARD_CHOICESS, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date  =  models.DateTimeField(null=True, blank=True)
    is_current = models.BooleanField(default=True)
    
    def __str__(self):
        return  "%s - %s" %(self.title, self.board)
    
    
class Holiday(models.Model):
    day = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    ay = models.ForeignKey(Ay, on_delete=CASCADE)
    center = models.ForeignKey(Center, blank=True, null=True)
    
    def __str__(self):
        return  "%s-%s" %(self.day, self.ay)
    
    

class Offering(models.Model):
    course = models.ForeignKey(Course, null=True, blank=True)
    center = models.ForeignKey(Center, null=True, blank=True)
    ay =  models.ForeignKey(Ay, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    topic = models.ManyToManyField(Topic, null=True, blank=True)
    status = models.IntegerField(choices=((1, 'pending'),(2, 'running'),(3, 'completed')), default=1)
    student = models.ManyToManyField(User, related_name='enrolled_students')
    teacher = models.ForeignKey(User, null=True, blank=True, related_name='current_teacher')
    batch = models.IntegerField(null=True, blank=True)
    program = models.IntegerField(choices=((0, 'None'),(1,'Digital Classroom'),(2,'LFH'),(3,'Worksheets'), (4,'Alumni'),(5,'Digital School')), default=0)
    
    @property
    def started_sessions(self):
        return Session.objects.filter(offering=self, status='started')

    @property
    def pending_sessions(self):
        return Session.objects.filter(offering=self, status='pending')

    def __str__(self):
        return '%s-%s' %(self.course, self.ay)

    

class Session(models.Model):
    
    STATUS_CHOICESS = ((1,'waiting'), (2,'scheduled'), (3,'completed'), (4,'rescheduled'),(5,'started'),(6,'cancelled'), (7,'Offline'))
    
    CANCLE_REASON_CHOICESS = ((1, 'Internet Down School'), (2, 'Power Cut School'), (3, 'Unscheduled leave School'), (4, 'Internet Down Teacher'),
     (5,'Power Cut Teacher'),(6,'Last Minute Dropout Teacher'), (7,'Communication Issue'), (8,'Teacher yet to be backfilled'), (9,'Others'))
    
    
    offering = models.ForeignKey(Offering, on_delete=CASCADE)
    topic = models.ManyToManyField(Topic, null=True, blank=True)
    subtopic = models.ForeignKey(SubTopic, null=True, blank=True)
    
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    teacher = models.ForeignKey(User, null=True, blank=True)
    
    status = models.IntegerField(choices=STATUS_CHOICESS, default=1)
    video = models.CharField(max_length=1024, null=True, blank=True)
    comment = models.TextField(max_length=2048, null=True, blank=True)
    cancel_reason = models.IntegerField(choices=CANCLE_REASON_CHOICESS, null=True, blank=True)
    ts_link = models.CharField(max_length=1024, blank=True)
    
    used_lesson_plan = models.BooleanField(default=True)

    def __str__(self):
        return '%s-%s :%s' %(self.start_date, self.end_date, self.teacher)
