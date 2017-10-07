from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def et_has_passed(time):
    return time <= timezone.localtime(timezone.now())
