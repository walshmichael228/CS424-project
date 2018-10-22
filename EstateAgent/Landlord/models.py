from django.db import models

class Member(models.Model):
    id_num = models.IntegerField(default=0)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
