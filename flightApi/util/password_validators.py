"""" custom validator for verifying password"""
import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


# pylint: disable=invalid-name,no-self-use,unused-argument
class NumberValidator:
    """Number Validator"""
    def validate(self, password, user=None):
        """validate if a password contains number"""
        if not re.findall(r'\d', password):
            raise ValidationError(
                _("Password must contain at least 1 digit."),
                code='password_no_number'
            )

    def get_help_text(self):
        """returns error message"""
        return _(
            "Your password must contain at least 1 digit"
        )


class UpperCaseValidator:
    """UpperCase Validator"""
    def validate(self, password, user=None):
        """validate if a password contains an uppercase letter"""
        if not re.findall(r'[A-Z]', password):
            raise ValidationError(
                _("Password must contain at least 1 uppercase letter"),
                code='password_no_upper'
            )

    def get_help_text(self):
        """returns error message"""
        return _(
            "Your password must contain at least 1 uppercase letter"
        )


class LowerCaseValidator:
    """Lowercase Validator"""
    def validate(self, password, user=None):
        """validate if a password contains a lowercase letter"""
        if not re.findall(r'[a-z]', password):
            raise ValidationError(
                _("Password must contain at least 1 lowercase letter"),
                code='password_no_lower'
            )

    def get_help_text(self):
        """returns error message"""
        return _(
            "Your password must contain at least 1 lowercase letter"
        )


class SymbolValidator:
    """Symbol Validator"""
    def validate(self, password, user=None):
        """validate if a password contains a symbol"""
        if not re.findall(r'[()[\]{}|`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("The password must contain at least 1 symbol"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        """returns error message"""
        return _(
            "Your password must contain at least 1 symbol: "
        )
