# expenses/backends.py
import logging
from django.contrib.auth.backends import ModelBackend
from .models import User

logger = logging.getLogger(__name__)


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        logger.debug(f"Authenticating user with email: {username}")
        try:
            user = User.objects.get(email=username)
            logger.debug(f"User found: {user.email}")
        except User.DoesNotExist:
            logger.debug(f"User with email {username} does not exist")
            return None

        if user.check_password(password):
            logger.debug(f"Password for user {username} is correct")
            return user
        else:
            logger.debug(f"Password for user {username} is incorrect")
        return None
