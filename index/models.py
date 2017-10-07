from django.db import models
from adminsortable.models import SortableMixin

# Create your models here.
class Officer(SortableMixin):
    name = models.CharField('Name', max_length=50)
    position = models.CharField('Position', max_length=30)
    username = models.CharField('Username', max_length=30, blank=True)
    email = models.EmailField('Email')
    website = models.URLField('Website', blank=True)
    github = models.URLField('GitHub', blank=True)
    linkedin = models.URLField('LinkedIn', blank=True)
    description = models.TextField('Description')
    picture = models.ImageField('Picture', upload_to='officers', blank=True)

    class Meta:
        ordering = ['officer_order']
        verbose_name_plural = None 

    officer_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return "Officer: " + self.name

class Event(models.Model):
    title = models.CharField('Name', max_length=80)
    time = models.DateTimeField('Date and Time')
    location = models.CharField('Location', max_length=50)
    description = models.TextField('Description')
    img = "title"

    class Meta:
        ordering = ['time']

    def __str__(self):
        return "Event: " + self.title
