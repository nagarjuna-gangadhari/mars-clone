from django.db import models
from taxonomy.models import BaseModel, Course, Topic, SubTopic, Language
from accounts.models import User
from django.utils.translation import gettext_lazy as _


class Question(BaseModel):

    """
    snippet: 
        {'type': '1',   'text':'', 'value':''}
        
        {'type': '2',   'text':'True, False', 'value':True}

        {'type': '3',   'text': {'1':'String', '2':'Intigers', '3':'Decimal', '4':'Boolean', '5':'Imagenary'}}

        {'type': '1',   'text': {     '1':'String', '2':'Intigers', '3':'Decimal', '4':'Boolean', '5':'Imagenary',
                                    'A':'String', 'B':'Intigers', 'C':'Decimal', 'D':'Boolean', '5':'Imagenary'
                                    }
                        'value': {'1':'A','2':'B','3':'C','4':'D'}
            }

    """


    class Type(models.IntegerChoices):
        OPEN = 1, _('text')
        YES_OR_NO = 2, _('bool')
        MULTIPLE = 3, _('option')
        FIB = 4, _('patren')


    course          = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    topic           = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    sub_topic       = models.ForeignKey(SubTopic, on_delete=models.DO_NOTHING)
    question        = models.TextField(null=True, blank=True)
    language        = models.ForeignKey(Language, on_delete=models.DO_NOTHING)
    type            = models.IntegerField(choices=Type.choices, default=Type.OPEN)
    snippet         = models.JSONField(null=True, blank=True)
    rubic_code      = models.IntegerField(null=True, blank=True)
    question_image  = models.ImageField(storage='/static/question/images/', null=True, blank=True)
    marks           = models.PositiveIntegerField(null=True, blank=True)



class Answer(models.Model):

    """_summary_

    answer: 
        {'type': '1', 'value':'bool'}

    Returns:
        str: pk
    """

    question    = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    answer      = models.JSONField(null=True, blank=True)
    marks       = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.pk)


class QuestionSet(BaseModel):

    question    = models.ManyToManyField(Question)
    answer      = models.ManyToManyField(Answer)

    def __str__(self):
        return str(self.pk)


class Assessment(BaseModel):
    """Assessments are used to track the progress of a student in their learning journey."""

    class Type(models.IntegerChoices):
        ONLINE = 1
        OFFLINE = 2

    question_set = models.ManyToManyField(QuestionSet)
    description = models.TextField('Description')
    start = models.DateTimeField()
    end = models.DateTimeField(auto_now=True)
    completed = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.DecimalField('Score', decimal_places=1, max_digits=4)
    type = models.IntegerField(choices=Type.choices, default=1)
    approved = models.BooleanField(default=True)

    def __str__(self):
        return str(self.pk)
    
