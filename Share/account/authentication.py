from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend


class EmailAuthBackend(BaseBackend):
    print('Email Auth class is called.')
    def authenticate(self, request, username=None, password=None):
        print('Email auth is called.')
        try:
            user = User.objects.get(email=username)
            if user.check_password(raw_password=password):

                return user
            return None
        except User.DoesNotExist:
            return None
    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None