from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager as BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django_prometheus.models import ExportModelOperationsMixin
from result import Ok, Err

from applications.common.models import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            return Err("The given username must be set")
        user = self.model(username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)

        return Ok(user)


class User(ExportModelOperationsMixin('user'), AbstractBaseUser, BaseModel):
    username = models.CharField(
        "username",
        max_length=150,
        unique=True,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[UnicodeUsernameValidator()],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    first_name = models.CharField("first name", max_length=150, blank=True)
    last_name = models.CharField("last name", max_length=150, blank=True)
    date_joined = models.DateTimeField("date joined", auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "username"

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    @property
    def full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()
