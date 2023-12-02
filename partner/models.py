from django.db import models
from accounts.models import User
from taxonomy.models import BaseModel, Ay


class Partner(BaseModel):

    class Type(models.IntegerChoices):
        VOLUNTEERING = 1
        DELIVERY = 2
        FUNDING = 3
        ORGANIZATION_UNIT = 4
        SCHOOL_ADMIN =5
        DIGITAL = 6

    class Status(models.IntegerChoices):
        NEW = 1
        IN_PROCESS = 2
        HOLD = 3
        APPROVED = 4
        REJECTED = 99

    class Source(models.IntegerChoices):
        WEBSITE = 1
        SOCIAL_MEDIA = 2
        OTHERS = 99

    class OrgType(models.IntegerChoices):
        TRUST = 1
        SOCIETY = 2
        CORPORATE = 3
        COMMUNITY = 4
        OTHERS = 99

    contactperson           = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='user_contactpersion')
    name                    = models.CharField(max_length=128, null=True, blank=True)
    organization            = models.CharField(max_length=256, null=True, blank=True)
    organization_type       = models.IntegerField(choices=OrgType.choices, default=OrgType.OTHERS)
    email                   = models.CharField(max_length=128, null=True, blank=True)
    phone                   = models.CharField(max_length=128, null=True, blank=True)
    address                 = models.CharField(max_length=512, null=True, blank=True)
    type                    = models.IntegerField(choices=Type.choices, null=True, blank=True)
    status                  = models.IntegerField(choices=Status.choices, default=Status.NEW)
    pam                     = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="pam_user")
    logo                    = models.FileField(upload_to='static/partner/logo', null=True, blank=True)
    source                  = models.IntegerField(choices=Source.choices, default=Source.WEBSITE)
    
    def __str__(self):
        return self.pk


class PartnerDetails(BaseModel):
    partner                 = models.ForeignKey(Partner, null=True, blank=True, on_delete=models.CASCADE, related_name="partner_details")
    website                 = models.CharField(max_length=128, null = True, blank=True)
    landline                = models.CharField(max_length=128, null = True, blank=True)
    signatory               = models.CharField(max_length=128, null = True, blank=True)
    registration_date       = models.DateField(null=True, blank=True)
    registration_place      = models.CharField(max_length=128, null=True, blank=True)
    registration_number     = models.CharField(max_length=128, null=True, blank=True)
    fcra_registration       = models.CharField(max_length=128, null=True, blank=True)
    fcra_account            = models.CharField(max_length=128, null=True, blank=True)
    bank_name               = models.CharField(max_length=128, null=True, blank=True)
    bank_ifsc               = models.CharField(max_length=128, null=True, blank=True)
    bank_account_holder     = models.CharField(max_length=128, null=True, blank=True)
    bank_account_number     = models.CharField(max_length=128, null=True, blank=True)
    bank_account_type       = models.CharField(max_length=128, null=True, blank=True)


class FundingHistory(BaseModel):
    partner                 = models.ForeignKey(Partner, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='partner_funding_history')
    ay                      = models.ForeignKey(Ay, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='partner_funding_history_ay')
    amount                  = models.IntegerField(default=0, null=True)
    requested_by            = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='partner_funding_history_requested')
    status                  = models.IntegerField(choices=((1,'Pending'),(2,'Accepted')),default=1)

