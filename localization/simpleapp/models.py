from django.db import models
from django.utils.translation import gettext as _


class Category(models.Model):
    # добавим переводящийся текст подсказку к полю
    name = models.CharField(max_length=100, help_text=_('category name'))
