from django.conf import settings
from django.contrib.auth import get_user_model


class EmailAuthentication(object):

    def authenticate(self, request, email=None, password=None):
        if '@' in email:
            kwargs = {'email__iexact': email}
        else:
            kwargs = {'username': email}
        try:
            user = get_user_model().objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, email):
        try:
            return get_user_model().objects.get(pk=email)
        except get_user_model().DoesNotExist:
            return None