from django.db import models
import datetime
from django.utils import timezone
from Users.models import Profile

class Petition(models.Model):
    CHOICES = (('Y', 'Yes'), ('N', 'No'), ('Nu', 'None'))
    voter = models.ManyToManyField(Profile)
    agenda = models.ForeignKey('Agenda', on_delete=models.CASCADE)
    choice = models.CharField('Choice', blank=True, null=True, max_length=50, choices=CHOICES)
    created_on = models.DateField("Created On", auto_now_add=True)    
    updated_on = models.DateField("Updated On", auto_now_add=True)

class Agenda(models.Model):
    STATUS_CHOICES = (('A', 'Active'), ('X', 'End'), ('W', 'Waiting'))
    agenda_text = models.CharField(max_length = 200, blank=True, null=True)
    status = models.CharField('Status', blank=True, null=True, max_length=1, choices=STATUS_CHOICES)
    ends_on = models.DateField("Deadline", blank=True, null=True)
    created_on = models.DateField("Created On", auto_now_add=True)
    updated_on = models.DateField("Updated On", auto_now_add=True)

