from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "user"


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_type = models.CharField(max_length=4)
    money = models.PositiveIntegerField()
    time = models.DateField()
    category = models.CharField(max_length=20)
    created_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "event"
