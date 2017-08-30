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
    description = models.CharField('Description', max_length=200)

    def __str__(self):
        return "Officer: " + self.name
