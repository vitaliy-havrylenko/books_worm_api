from django.contrib import admin
from apps.accounts.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    list_display = ('pk', 'username', 'phone_number', 'email', 'first_name',
                    'is_staff', 'is_superuser', 'is_active', 'is_email_validated', 'avatar', 'token')
    # filter_horizontal = ('favorites', 'favorite_authors', )

    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        (_('Personal info'), {'fields': ('username', 'first_name', 'email', 'token')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser','is_email_validated', 'groups', 'user_permissions')}),
        # (_('Fav books'), {'fields': ('favorites', )}),
        # (_('Fav authors'), {'fields': ('favorite_authors',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2'),
        }),
    )

    def phone_number(self):
        return self.phone_number


admin.site.register(User, UserAdmin)

