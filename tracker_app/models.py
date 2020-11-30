from django.contrib.auth.models import AbstractUser

from django.db import models

from django.utils import timezone
# Create your models here.


class CustUser(AbstractUser):
    name = models.CharField(max_length=150, null=True)

    def __str__(self):
        return f'{self.name}'


class Tickets(models.Model):

    Status_Of_Tickets = [
        ('NW', 'New'),
        ('IP', 'In Progress'),
        ('DN', 'Done'),
        ('IV', 'Invalid'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    date_filed = models.DateTimeField(default=timezone.now)
    user_assign = models.ForeignKey(CustUser, on_delete=models.CASCADE, related_name='user_ass')
    user_filed = models.ForeignKey(CustUser, on_delete=models.CASCADE, related_name='user_fill')
    user_complete = models.ForeignKey(CustUser, on_delete=models.CASCADE, related_name='user_complete')
