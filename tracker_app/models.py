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
        ('NEW', 'new'),
        ('IN_PROGRESS', 'in_progress'),
        ('DONE', 'done'),
        ('INVALID', 'invalid'),
    ]

    status = models.CharField(max_length=12, choices=Status_Of_Tickets, default='NEW')
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_filed = models.DateTimeField(default=timezone.now)
    user_filed = models.ForeignKey(CustUser, on_delete=models.CASCADE, related_name='user_filed', null=True)
    user_assigned = models.ForeignKey(CustUser, on_delete=models.CASCADE, related_name='user_ass', null=True)
    user_completed = models.ForeignKey(CustUser, on_delete=models.CASCADE, related_name='user_completed', null=True)