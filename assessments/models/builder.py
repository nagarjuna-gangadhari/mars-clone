from django.db import models
from taxonomy.models import BaseModel, Course, Topic, SubTopic, Language
from accounts.models import User
from django.utils.translation import gettext_lazy as _
from random import sample
from taggit.managers import TaggableManager
import pandas as pd
import json


class Question(BaseModel):

    """
    snippet:
        {'type': '1',   'text':'', 'value':''}

        {'type': '2',   'text': {'1':True, '2':False}, 'value':True}

        {'type': '3',   'text': {'1':'String', '2':'Intigers', '3':'Decimal', '4':'Boolean', '5':'Imagenary'},
                        'value':'1'
            }

        {'type': '1',   'text': { '1':'String', '2':'Intigers', '3':'Decimal', '4':'Boolean', '5':'Imagenary',
                                  'A':'String', 'B':'Intigers', 'C':'Decimal', 'D':'Boolean', 'c':'Imagenary'
                                },
                        'value': {'1':'A','2':'B','3':'C','4':'D','5':'C'}
            }
    """

    class Type(models.IntegerChoices):
        OPEN = 1, _("text")
        YES_OR_NO = 2, _("bool")
        MULTIPLE = 3, _("option")
        FIB = 4, _("patren")

    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    sub_topic = models.ForeignKey(SubTopic, on_delete=models.DO_NOTHING)
    points = models.FloatField(default=1.0)
    summary = models.CharField(max_length=256, null=True, blank=True)
    question = models.TextField(null=True, blank=True)
    solution = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING)
    type = models.IntegerField(choices=Type.choices, default=Type.OPEN)
    rubic_code = models.IntegerField(null=True, blank=True)
    min_time = models.IntegerField("time in minutes", default=0)
    question_image = models.ImageField(
        storage="/static/question/images/", null=True, blank=True
    )
    marks = models.PositiveIntegerField(null=True, blank=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return str(self.pk)


class MultipleChoiceOptions(BaseModel):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    option_a = models.CharField(max_length=1024, null=True, blank=True)
    option_b = models.CharField(max_length=1024, null=True, blank=True)
    option_c = models.CharField(max_length=1024, null=True, blank=True)
    option_d = models.CharField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return str(self.pk)


class PatrenOptions(BaseModel):

    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    option_1 = models.CharField(max_length=1024, null=True, blank=True)
    option_2 = models.CharField(max_length=1024, null=True, blank=True)
    option_3 = models.CharField(max_length=1024, null=True, blank=True)
    option_4 = models.CharField(max_length=1024, null=True, blank=True)
    option_a = models.CharField(max_length=1024, null=True, blank=True)
    option_b = models.CharField(max_length=1024, null=True, blank=True)
    option_c = models.CharField(max_length=1024, null=True, blank=True)
    option_d = models.CharField(max_length=1024, null=True, blank=True)


class Answer(models.Model):

    """
    answer:
        {'type': '1',   'text':'', 'value':''}

        {'type': '2',   'text': {'1':True, '2':False}, 'value':True}

        {'type': '3',   'text': {'1':'String', '2':'Intigers', '3':'Decimal', '4':'Boolean', '5':'Imagenary'},
                        'value':'1'
            }

        {'type': '1',   'text': { '1':'String', '2':'Intigers', '3':'Decimal', '4':'Boolean', '5':'Imagenary',
                                  'A':'String', 'B':'Intigers', 'C':'Decimal', 'D':'Boolean', 'c':'Imagenary'
                                },
                        'value': {'1':'A','2':'B','3':'C','4':'D','5':'C'}
            }
    """

    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, related_name='qsans')
    # The answer submitted by the user.
    answer = models.TextField(null=True, blank=True)
    correct = models.BooleanField(default=False)
    skipped = models.BooleanField(default=False)
    comment = models.TextField(null=True, blank=True)
    marks = models.PositiveIntegerField(null=True, blank=True)

    def set_marks(self, marks):
        if marks > self.question.points:
            self.marks = self.question.points
        else:
            self.marks = marks

    def set_comment(self, comments):
        self.comment = comments

    def __str__(self):
        return str(self.pk)


class QuestionPaper(models.Model):
    """Question set contains a set of questions from which random questions
    will be selected for the quiz.
    """

    total_marks = models.FloatField(null=True, blank=True)
    questions = models.ManyToManyField(Question)
    shuffle_questions = models.BooleanField(default=False, blank=False)

    def get_questions_count(self):
        return self.questions.all().count()

    def get_random_questions(self):
        """Returns random questions from set of questions"""
        return sample(list(self.questions.all()), self.num_questions)

    def __str__(self):
        return str(self.pk)


class Assessment(BaseModel):
    """Assessments are used to track the progress of a student in their learning journey."""

    class Type(models.IntegerChoices):
        ONLINE = 1
        OFFLINE = 2

    question_set = models.ForeignKey(QuestionPaper, on_delete=models.DO_NOTHING, related_name='assQst')
    description = models.TextField("Description")
    start = models.DateTimeField()
    end = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField(null=True, blank=True)
    mode = models.IntegerField(choices=Type.choices, default=1)
    approved = models.BooleanField(default=True)

    def __str__(self):
        return str(self.pk)


class AnswerPaper(models.Model):
    """A answer paper for a student -- one per student typically."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='examstudent')
    question_paper = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='qstoans')
    answers = models.ManyToManyField(Answer, related_name='aspans')
    attempt_number = models.IntegerField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    # User's IP which is logged.
    user_ip = models.CharField(max_length=255)

    # Teacher comments on the question paper.Answer
    comments = models.TextField(null=True, blank=True)

    marks_obtained = models.FloatField(null=True, blank=True, default=0.0)
    passed = models.BooleanField(default=True)
    extra_time = models.FloatField("Additional time in mins", default=0.0)
    is_special = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "question_paper", "attempt_number")

    def get_score(self, question_ids):
        if not question_ids:
            return None
        que_ids = list(zip(*question_ids))[1]
        answers = self.answers.filter(question_id__in=que_ids).values(
            "question_id", "marks"
        )
        que_data = {}
        df = pd.DataFrame(answers)
        ans_data = None
        if not df.empty:
            ans_data = df.groupby("question_id").tail(1)
        for que_summary, que_id, que_comments in question_ids:
            if ans_data is not None:
                ans = ans_data["question_id"].to_list()
                marks = ans_data["marks"].to_list()
                if que_id in ans:
                    idx = ans.index(que_id)
                    que_data[que_summary] = marks[idx]
                else:
                    que_data[que_summary] = 0
            else:
                que_data[que_summary] = 0
            que_data[que_comments] = "NA"
        return que_data

    def get_unanswred_questions_count(self):
        """Returns the number of questions left."""
        return None

    def time_left(self):
        """Return the time remaining for the user in seconds."""

        return 0

    def time_left_on_question(self, question):
        secs = self._get_total_seconds()
        total = question.min_time * 60.0
        remain = max(total - secs, 0)
        return int(remain)

    def _update_percent(self):
        """Updates the percent gained by the student for this paper."""
        total_marks = self.question_paper.total_marks
        if self.marks_obtained is not None:
            percent = self.marks_obtained / total_marks * 100
            self.percent = round(percent, 2)

    def _update_status(self, state):
        """Sets status as inprogress or completed"""
        self.status = state

    def update_marks(self, state="completed"):
        self._update_percent()
        self._update_status(state)
        self.save()

    def get_question_answers(self):
        """
        Return a dictionary with keys as questions and a list of the
        corresponding answers.
        """
        q_a = {}
        for question in self.questions.all():
            answers = question.answer_set.filter(answerpaper=self).distinct()
            if not answers.exists():
                q_a[question] = [None, 0.0]
                continue
            ans_errs = []
            for answer in answers:
                ans_errs.append(
                    {
                        "answer": answer,
                        "error_list": [e for e in json.loads(answer.error)],
                    }
                )
            q_a[question] = ans_errs
            q_a[question].append(self._get_marks_for_question(question))
        return q_a

    def get_questions(self):
        return self.questions.filter(active=True)

    def __str__(self):
        return str(self.pk)
