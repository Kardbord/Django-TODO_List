from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TODO_Item(models.Model):
    description = models.TextField('Description', max_length=300)
    title = models.CharField('Title', max_length=50)
    due_date = models.DateTimeField('Due Date')
    isComplete = models.BooleanField('is completed', default=False)
    priority = models.CharField(max_length=3, choices=PRIORITIES)
    
PRIORITIES = (
    ('HIG', 'high'),
    ('MED', 'medium'),
    ('LOW', 'low'),
)