from django.utils import timezone
from datetime import timedelta

class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    phone_verified = models.BooleanField(default=False)
    phone_code = models.CharField(max_length=6, blank=True, null=True)
    phone_code_expires = models.DateTimeField(blank=True, null=True)

    def set_phone_code(self, code):
        self.phone_code = code
        self.phone_code_expires = timezone.now() + timedelta(minutes=3)
        self.save()

    def verify_phone_code(self, code):
        if self.phone_code != code:
            return False
        if timezone.now() > self.phone_code_expires:
            return False
        self.phone_verified = True
        self.phone_code = None
        self.phone_code_expires = None
        self.save()
        return True
