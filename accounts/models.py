from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .validators import UnicodeUsernameIdValidator
from django.conf import settings
from taxonomy.models import BaseModel


class User(AbstractUser):
    username_validator = UnicodeUsernameIdValidator()
    username = models.CharField(
        _("username"),
        max_length=12,
        unique=True,
        help_text=_("Required, User id only."),
        validators=[username_validator],
        error_messages={
            "unique": _("Username Exists."),
        },
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            last_username = User.objects.all().values_list("username", flat=True).last()
            if last_username:
                new_username = int(last_username) + 1
            else:
                new_username = settings.USERID_BASE + 1
            self.username = new_username
            super(User, self).save(*args, **kwargs)
        else:
            super(User, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.username)


class Profile(BaseModel):
    class Profession(models.IntegerChoices):
        SELF_EMPLOYED = 1
        HOME_MAKER = 2
        AGRICULTURE = 3
        MEDICAL = 4
        LAW = 5
        ENGINEERING = 6
        SERVICE = 7
        PSU = 8
        STUDENT = 9
        TEACHING = 10
        OTHERS = 99

    class Education(models.IntegerChoices):
        PHD = 1
        POST_GRADUATION = 2
        UNDER_GRADUATION = 3
        dIPLOMA = 4
        HIGH_SCHOOL = 5
        OTHERS = 99

    class Gender(models.IntegerChoices):
        Male = 1
        Female = 2
        Others = 99

    user = models.OneToOneField("accounts.User", related_name="user", on_delete=models.CASCADE)
    terms = models.BooleanField(default=False)
    reference = models.ForeignKey("accounts.User", null=True, blank=True, related_name="referer", on_delete=models.DO_NOTHING)
    dob = models.DateField(null=True, blank=True)
    mobile = models.CharField(max_length=12, null=True, blank=True)
    gender = models.IntegerField(choices=Gender.choices, default=100)
    location = models.ForeignKey("taxonomy.Location", null=True, blank=True, related_name="location", on_delete=models.DO_NOTHING)
    pincode = models.IntegerField(null=True, blank=True)
    profession = models.IntegerField(choices=Profession.choices, default=100)
    education = models.IntegerField(choices=Education.choices, default=100)
    linkedIn = models.CharField(max_length=256, null=True, blank=True)
    step = models.IntegerField(default=1)   
    about = models.TextField(null=True, blank=True)
    language = models.ForeignKey('taxonomy.Language', null=True, blank=True, on_delete=models.DO_NOTHING)
    is_email_verified = models.BooleanField(default=False)
    activation_key = models.CharField(max_length=255, blank=True, null=True)
    key_expiry_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "%s-%s :%s" % (self.id, self.user.id, self.user.email)



class Role(BaseModel):

    name = models.CharField(max_length=128, null=False, blank=False)
    type = models.IntegerField('Type', 'INTERNAL EXTERNAL', null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)


class UserRoleMaping(BaseModel):

    class Status(models.IntegerChoices):
        NOT_OPTED = 1
        OPTED = 2
        POST_DISCUSSION = 3
        SCHEDULED = 4
        IN_REVIEW = 5
        RECOMMENDED = 6
        REJECTED = 99

    user = models.ForeignKey('accounts.User', related_name='role_map_user', on_delete=models.CASCADE)
    role = models.ForeignKey('accounts.Role', related_name='role_maping', on_delete=models.CASCADE)
    combo = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING)
    status = models.IntegerField(choices=Status.choices, default=1)
    meetingLink = models.CharField(max_length=256, null=True, blank=True)
    meeting = models.ForeignKey('accounts.UserRoleMeeting', null=True, blank=True, on_delete=models.DO_NOTHING)
    recommendedOn = models.DateTimeField(null=True, blank=True)
    notes = models.CharField(max_length=256, null=True, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)
    

class UserRoleMeeting(models.Model):
    class Outcome(models.IntegerChoices):
        SCHEDULED = 1
        ASSAIGNED = 2
        COMPLETED = 3
        CANCELLED = 99
        
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    role = models.ForeignKey(Role, null=True, blank=True, default=None, on_delete=models.CASCADE)
    panel = models.ForeignKey(User, null=True, blank=True, related_name="panel_member", on_delete=models.DO_NOTHING)
    date = models.DateTimeField(null=True,blank=True)
    start_time = models.DateTimeField(null=True,blank=True)
    end_time = models.DateTimeField(blank=True, null=True)
    # meetingLink = models.CharField(max_length=256, null=True, blank=True)
    outcome = models.IntegerField('Status', 'RECOMMENDED NOT_RECOMMENDED', null=True, blank=True)
    status = models.IntegerField(choices=Outcome.choices, default=1)

    def __str__(self):
        return str(self.pk)


class RoleHistory(BaseModel):
    role = models.ForeignKey('accounts.Role', related_name='role_history', on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    role_map = models.ForeignKey('accounts.UserRoleMaping', null=True, blank=True, on_delete=models.DO_NOTHING)
    note = models.CharField(max_length=256, null=True, blank=True)
    map_object = models.JSONField(null=True, blank=True)


class NotificationPreference(BaseModel):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.BooleanField(default=False)
    sms = models.BooleanField(default=False)
    watsapp = models.BooleanField(default=False)