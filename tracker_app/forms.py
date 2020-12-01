from django import forms

from tracker_app.models import CustUser


class AddTicket(forms.Form):

    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)


class EditTicket(forms.Form):

    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)


class LoginForm(forms.Form):

    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class ActionForm(forms.Form):

    pick_user = forms.ModelChoiceField(queryset=CustUser.objects.all())
