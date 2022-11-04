from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from.forms import CustomCreationsForm, CustomChangeForm

#admin.site.register(CustomUser, CustomUserAdmin)
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomChangeForm
    FORM = CustomCreationsForm
    list_display = ('email')

