from django.contrib.auth.models import BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not phone_number:
            raise ValueError('This object requires an phone number')

        user = self.model(phone_number=phone_number, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_superuser(self, phone_number, password):

        user = self.create_user(phone_number, password)
        user.is_staff = True

        user.is_superuser = True
        user.save(using=self._db)
        return user

