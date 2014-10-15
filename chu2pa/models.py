from django.contrib.auth.models import AbstractUser
from django.db import models


class UserStatus(AbstractUser):
    TITLE_CHOICES = (
                    ('T', 'Teacher'),
                    ('S', 'Student'),
                 )

    title = models.CharField(max_length=200, choices=TITLE_CHOICES, default="S")


class Calendar(models.Model):
    date = models.CharField(max_length=100)
    person = models.ForeignKey(UserStatus, related_name="person")
    status = models.BooleanField(default=False)

    def __unicode__(self):
        return self.date
