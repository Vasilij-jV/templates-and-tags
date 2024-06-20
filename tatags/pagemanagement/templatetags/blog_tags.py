from django import template
from ..models import Page
import random

register = template.Library()


@register.simple_tag
def total_pages():
    return Page.objects.values('title').count()


@register.simple_tag
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"
