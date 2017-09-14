from django.db import models

# Create your models here.
class Officer(models.Model):
    name = models.CharField('Name', max_length=50)
    position = models.CharField('Position', max_length=30)
    username = models.CharField('Username', max_length=30, blank=True)
    email = models.EmailField('Email')
    website = models.URLField('Website', blank=True)
    github = models.URLField('GitHub', blank=True)
    linkedin = models.URLField('LinkedIn', blank=True)
    description = models.TextField('Description')

    def __str__(self):
        return "Officer: " + self.name

class Event(models.Model):
    title = models.CharField('Name', max_length=80)
    time = models.DateTimeField('Date and Time')
    location = models.CharField('Location', max_length=50)
    description = models.TextField('Description')

    def __str__(self):
        return "Event: " + self.title
