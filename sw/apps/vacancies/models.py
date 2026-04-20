from django.contrib.auth.models import User
from django.db import models

class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
