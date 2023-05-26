from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from account.manager import UserManager



class User(AbstractUser):

    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)

    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



# Create your models here.
