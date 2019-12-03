import uuid
from django.core.exceptions import ValidationError
from string import digits
from phonenumber_field.modelfields import PhoneNumberField as OriginalPhoneNumberField, to_python
import phonenumbers as pn
from django.utils.translation import ugettext_lazy as _
from django.utils.crypto import get_random_string


def is_possible_phonenumber(value):
    phone_number = to_python(value)
    if phone_number and not pn.is_possible_number(phone_number):
        raise ValidationError(_(u'The phone number entered is not possible.'))


class PhoneNumberField(OriginalPhoneNumberField):
    default_validators = [is_possible_phonenumber]


def get_validation_code():
    return get_random_string(length=4, allowed_chars=digits)


def handle_photo_upload(instance, filename) -> str:
    bits = str(instance.pk)
    return 'account/{0}/{1}/{2}'.format(bits[:2], bits[2:4], filename)
