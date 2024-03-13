from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст мероприятия')



