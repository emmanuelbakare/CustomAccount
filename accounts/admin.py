from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from accounts.models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""

    # model = CustomUser

    fieldsets = (
        (None, {'fields': ('email','phone' )}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone','password1', 'password2'),
        }),
    )
    list_display = ('email', 'phone','first_name', 'last_name', 'is_staff')
    search_fields = ('email','phone', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(get_user_model(),CustomUserAdmin)
