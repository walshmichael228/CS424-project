from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    id_num = models.IntegerField(default=0)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user = models.OneToOneField(User, blank=True, null=True, on_delete = models.CASCADE)
