from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager



class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that uses phone_number instead of username"""

    phone_number = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'phone_number'

    def save(self, *args, **kwargs):
        if 'sha256' not in self.password:
            self.set_password(self.password)

        return super().save(*args,**kwargs)

