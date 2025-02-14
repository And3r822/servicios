from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, db_column='email', max_length=100)
    username = models.CharField(max_length=50, unique=True, db_column='username')
    password = models.CharField(max_length=150, db_column='password')
    groups = models.ManyToManyField(Group, related_name='custom_users_groups')  # Cambiado
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users_permissions')  # Cambiado

    class Meta:
        db_table = 'usuarios'