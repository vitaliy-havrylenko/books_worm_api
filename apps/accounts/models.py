from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from apps.accounts.utils import PhoneNumberField
# from books_app.models import Book, Author
from versatileimagefield.fields import VersatileImageField
from apps.accounts.utils import handle_photo_upload
from apps.core.models import CoreModel
from .managers import UserManager


class User(PermissionsMixin, CoreModel, AbstractBaseUser):
    username = models.CharField(_('username'), max_length=100, unique=True, null=True)
    phone_number = PhoneNumberField(_('Phone number'), unique=True, null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True, null=True, blank=True)
    first_name = models.CharField(_('first_name'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_email_validated = models.BooleanField(_('email_validated'), default=False)
    avatar = VersatileImageField(
        'user avatar',
        upload_to=handle_photo_upload,
        max_length=255,
        null=True,
        blank=True
    )
    token = models.CharField(max_length=36, unique=True, null=True)
    # favorites = models.ManyToManyField(Book, blank=True)
    # favorite_authors = models.ManyToManyField(Author, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __repr__(self):
        return self.username
