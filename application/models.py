from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

from application.managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username",)

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Repository(models.Model):
    authorNames = models.TextField()
    description = models.TextField()
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
