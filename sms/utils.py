from django.core.exceptions import ValidationError
from string import digits
from phonenumber_field.modelfields import (to_python, PhoneNumberField as
                                           OriginalPhoneNumberField)
import phonenumbers
from django.utils.translation import ugettext_lazy as _
from django.utils.crypto import get_random_string


def is_possible_phonenumber(value):
    phone_number = to_python(value)
    if phone_number and not phonenumbers.is_possible_number(phone_number):
        raise ValidationError(_(u'The phone number entered is not possible.'))


class PhoneNumberField(OriginalPhoneNumberField):
    default_validators = [is_possible_phonenumber]


def get_validation_code():
    return get_random_string(length=4, allowed_chars=digits)
