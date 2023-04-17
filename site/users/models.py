from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    photo = models.ImageField(upload_to='users_images/', verbose_name='Фото пользователя', null=True, blank=True)
