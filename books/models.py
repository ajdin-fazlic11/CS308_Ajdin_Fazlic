from django.db import models

# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=35, blank=True, default='')
    authors = models.CharField(max_length=100, blank=True, default='')
    publisher = models.CharField(max_length=35, blank=True, default='')
    publication_date = models.DateField(blank=True, default='')
    number_of_pages = models.IntegerField(blank=True, default='')

    class Meta:
        ordering = ['created']