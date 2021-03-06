from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

# Create your models here.

PRIORITIES = (
    ('HIG', 'High'),
    ('MED', 'Medium'),
    ('LOW', 'Low'),
)

class TODO_Item(models.Model):
    description = models.TextField('Description', max_length=500)
    title = models.CharField('Title', max_length=100)
    due_date = models.DateTimeField('Due Date')
    isComplete = models.BooleanField('is completed', default=False)
    priority = models.CharField(max_length=3, choices=PRIORITIES)
    
    def __str__(self):
        return self.title
        
        
class TODO_Item_Form(ModelForm):
    class Meta:
        model = TODO_Item
        fields = ['title', 'due_date', 'priority', 'description', 'isComplete']