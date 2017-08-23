from django.db import models

# Create your models here.
class Officer(models.Model):
    name = models.CharField('Name', max_length=50)
    position = models.CharField('Position', max_length=30)
    username = models.CharField('Username', max_length=30)
    email = models.EmailField('Email')
    website = models.URLField('Website')
    github = models.URLField('GitHub')
    linkedin = models.URLField('LinkedIn')
    description = models.CharField('Description', max_length=200)
