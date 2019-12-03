from uuid import uuid4
from django.db import models
from django.utils.translation import gettext_lazy as _


class CoreQuerySet(models.QuerySet):

    def active(self):
        return self.filter(is_active=True)

    def inactive(self):
        return self.filter(is_active=False)


class CoreManager(models.Manager):

    def get_queryset(self):
        return CoreQuerySet(self.model, using=self._db)


class CoreModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'),
                                   db_index=True)
    updated = models.DateTimeField(auto_now=True, verbose_name=_('updated'))
    is_active = models.BooleanField(default=True, db_index=True)

    objects = CoreManager()

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)
