from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    uid = models.CharField(max_length=12, unique=True, blank=True, null = True)
    mobile = models.CharField(max_length=10, unique = True, blank = True, null = True)
    t_and_c = models.BooleanField('Accepted terms', blank=True, null=True, default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)