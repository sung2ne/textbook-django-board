import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, blank=True, null=True)

    def generate_email_token(self):
        self.email_token = str(uuid.uuid4())
        self.save()
        return self.email_token
