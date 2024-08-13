from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from datetime import date
from users.manager import UserManagement
# Create your models here.


class Users(AbstractUser):
    email = models.EmailField(_('email address'),  unique= True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    
    objects = UserManagement()
    
    def __str__(self):
        return self.email