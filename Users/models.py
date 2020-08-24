from django.db import models
from polls.models import Question
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=50, default='Your First Name is currently is empty')
    last_name = models.CharField(max_length=50 , default='Your Last Name is currently is empty')
    Address = models.CharField(max_length=300 , default='Your Address is currently is empty')
    P_no = models.IntegerField(default=None, blank=True, null=True)
    Dob = models.DateField(default=None, blank=True, null=True)
    

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)