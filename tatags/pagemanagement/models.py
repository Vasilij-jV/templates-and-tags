from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Variables(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    objects = models.Manager()


class Page(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('pagemanagement:edit_page', args=[self.slug])

    def __str__(self):
        return self.title
