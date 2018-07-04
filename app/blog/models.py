from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    content = models.TextField(blank=True)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title