import os
from django.test import TestCase
from django.conf import settings
from django.contrib.auth.password_validation import validate_password

class TryDjangoConfTest(TestCase):
    def test_secret_key_strenght(self):
        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f'Bad Secret key {e.messages}'
            self.fail(msg)
