from django.contrib.auth.tokens import PasswordResetTokenGenerator
from records.models import Citizen
import six


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, citizen, timestamp):
        return (
            six.text_type(citizen.pk) + six.text_type(timestamp) +
            six.text_type(True)
        )


account_activation_token = TokenGenerator()