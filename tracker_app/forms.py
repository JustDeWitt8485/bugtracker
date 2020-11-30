from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from django import forms

from tracker_app.models import Tickets


class DetailUserForm(UserChangeForm):

    name = forms.CharField(max_length=150)


class AddTicket(forms.Form):

    Status_Of_Tickets = [
            ('NW', 'New'),
            ('IP', 'In Progress'),
            ('DN', 'Done'),
            ('IV', 'Invalid'),
        ]
    ticket = forms.ModelChoiceField(queryset=Tickets.objects.all())
    title = forms.CharField(max_length=200)
    description = forms.TimeField()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
