from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=200)
    # time = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title
