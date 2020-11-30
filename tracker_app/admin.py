from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tracker_app.models import CustUser, Tickets
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

# Register your models here.


ADDITIONAL_USER_FIELD = (
    (None, {'fields': ('name',)}),
)


class CustomUserAdmin(UserAdmin):
    user_create_form = UserCreationForm
    user_change_form = UserChangeForm
    view = ['username', 'name']
    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELD
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELD


admin.site.register(CustUser, CustomUserAdmin)
admin.site.register(Tickets)
