from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField('Name', max_length=80)
    time = models.DateTimeField('Date and Time')
    description = models.TextField('Description')

    def __str__(self):
        return "Event: " + self.title
