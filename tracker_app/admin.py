from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tracker_app.models import CustUser, Tickets

# Register your models here.


ADDITIONAL_USER_FIELD = (
    (None, {'fields': ('name',)}),
)


class CustomUserAdmin(UserAdmin):
    view = ['username', 'name']
    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELD
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELD


admin.site.register(CustUser, CustomUserAdmin)
admin.site.register(Tickets)
