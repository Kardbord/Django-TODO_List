from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TODO_Item(models.Model):
    description = models.CharField('Description', max_length=200)
    title = models.CharField('Title', max_length=50)
    due_date = models.DateField('Due_Date')
    # TODO: add priority