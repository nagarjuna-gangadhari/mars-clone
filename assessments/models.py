from django.db import models
from taxonomy.models import BaseModel

class Question(BaseModel):
    question        = models.TextField(null=True, blank=True)
    question_image  = models.ImageField(storage='/static/question/images/')
    marks           = models.PositiveIntegerField()


class OpenQuestion(Question):
    answer = models.TextField(null=True, blank=True)


class MultipleChoice(Question):

    class Answer(models.IntegerChoices):
        OPTION1 = 1
        OPTION2 = 2
        OPTION3 = 3
        OPTION4 = 4

    option1 = models.CharField(max_length=512, null=True, blank=True)
    option2 = models.CharField(max_length=512, null=True, blank=True)
    option3 = models.CharField(max_length=512, null=True, blank=True)
    option4 = models.CharField(max_length=512, null=True, blank=True)
    answer  = models.IntegerField(choices=Answer.choices, default=1)


class Matching(Question):

    class Answer(models.IntegerChoices):
        PATREN1 = 1, {1:5, 2:6, 3:7, 4:8}
        PATREN2 = 2, {1:5, 2:6, 3:8, 4:7}
        PATREN3 = 3, {1:5, 2:7, 3:6, 4:8}
        PATREN4 = 4, {1:5, 2:7, 3:8, 4:6}
        PATREN5 = 5, {1:5, 2:8, 3:7, 4:5}
        PATREN6 = 6, {1:5, 2:8, 3:5, 4:7}
        PATREN7 = 7, {1:6, 2:7, 3:8, 4:5}
        PATREN8 = 8, {1:6, 2:7, 3:5, 4:8}
        PATREN9 = 9, {1:6, 2:8, 3:5, 4:7}
        PATREN10 = 10, {1:6, 2:8, 3:7, 4:5}
        PATREN11 = 11, {1:7, 2:8, 3:5, 4:6}
        PATREN12 = 12, {1:7, 2:8, 3:6, 4:5}
        PATREN13 = 13, {1:7, 2:6, 3:7, 4:5}
        PATREN14 = 14, {1:7, 2:6, 3:5, 4:7}
        PATREN15 = 15, {1:7, 2:5, 3:6, 4:8}
        PATREN16 = 16, {1:7, 2:5, 3:8, 4:6}
        PATREN17 = 17, {1:8, 2:7, 3:5, 4:6}
        PATREN18 = 18, {1:8, 2:7, 3:6, 4:5}
        PATREN19 = 19, {1:8, 2:6, 3:7, 4:5}
        PATREN20 = 20, {1:8, 2:6, 3:5, 4:7}
        PATREN21 = 21, {1:8, 2:8, 3:6, 4:7}
        PATREN22 = 22, {1:8, 2:8, 3:7, 4:6}

    option1 = models.CharField(max_length=512, null=True, blank=True)
    option2 = models.CharField(max_length=512, null=True, blank=True)
    option3 = models.CharField(max_length=512, null=True, blank=True)
    option4 = models.CharField(max_length=512, null=True, blank=True)
    option5 = models.CharField(max_length=512, null=True, blank=True)
    option6 = models.CharField(max_length=512, null=True, blank=True)
    option7 = models.CharField(max_length=512, null=True, blank=True)
    option8 = models.CharField(max_length=512, null=True, blank=True)
    answer  = models.IntegerField(choices=Answer.choices, default=1)     


class FillInTheBlank(Question):

    answer  = models.JSONField(null=True, blank=True)





class Assessment(BaseModel):
    """Assessments are used to track the progress of a student in their learning journey."""
    class Meta:
        verbose_name = 'assessment'
        verbose_name_plural = 'assessments'
    
    name = models.CharField('Name', max_length=256)
    description = models.TextField('Description')
    date = models.DateTimeField('Date')
    score = models.DecimalField('Score', decimal_places=1, max_digits=4)
    # TODO: Add foreign key for course and user (student)

    def __str__(self):
        return self.name
    

