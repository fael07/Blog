from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from Support.Code.django.forms.accounts import UserChangeForm, UserCreationForm
from accounts.models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos adicionais", {"fields": ('name', 'slug', "photo")}),
    )
    list_display = 'icon', 'first_name', 'username'
    list_display_links = 'first_name', 'username'
