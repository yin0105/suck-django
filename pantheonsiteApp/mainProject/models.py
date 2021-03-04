from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInformations(models.Model):
    class Meta:
        db_table = 'user_profiles'
    user = models.OneToOneField(User, primary_key=True, related_name='user_profiles', on_delete = models.CASCADE)

    company = models.IntegerField()
    title = models.CharField(max_length=255)
    role= models.IntegerField(default=2)
    email_verify = models.BooleanField(default=False)
    email_token = models.CharField(max_length=255, blank=True, null=True)
    email_image = models.CharField(max_length=255, blank=True, null=True)
    google_auth_verify = models.BooleanField(default=False)
    google_auth_provide_id = models.CharField(max_length=255, blank=True, null=True)
    google_auth_email = models.CharField(max_length=255, blank=True, null=True)
    google_auth_name = models.CharField(max_length=255, blank=True, null=True)
    google_auth_image = models.CharField(max_length=255, blank=True, null=True)
    linkedin_auth_verify = models.BooleanField(default=False)
    linkedin_auth_provide_id = models.CharField(max_length=255, blank=True, null=True)
    linkedin_auth_email = models.CharField(max_length=255, blank=True, null=True)
    linkedin_auth_name =models.CharField(max_length=255, blank=True, null=True)
    linkedin_auth_image =models.CharField(max_length=255, blank=True, null=True)
    outlook_auth_verify = models.BooleanField(default=False)
    outlook_auth_provide_id = models.CharField(max_length=255, blank=True, null=True)
    outlook_auth_email = models.CharField(max_length=255, blank=True, null=True)
    outlook_auth_name = models.CharField(max_length=255, blank=True, null=True)
    outlook_auth_image = models.CharField(max_length=255, blank=True, null=True)
    real_password = models.CharField(max_length=255)

    def __str__(self):
        self.user.is_active=True
        self.user.save()
        return str(self.user.id)
    

