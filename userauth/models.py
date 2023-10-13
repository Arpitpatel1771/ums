from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from core_django.models import BaseModel

class PermissionGroup(BaseModel):
    name = models.TextField()
    code = models.TextField()
    description = models.TextField(null=True)

class User(BaseModel, AbstractUser):
    first_name = models.TextField(null=True)
    middle_name = models.TextField(null=True)
    last_name = models.TextField(null=True)

    permission_groups = models.ManyToManyField(
        PermissionGroup,
        blank=True,
        related_name="users",
    )
