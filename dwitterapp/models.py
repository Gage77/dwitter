from django.db import models
from django.utils import timezone
import arrow


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=140)
    create_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    attachment = models.FileField(upload_to='documents/')

    def publish(self):
        self.published_date = arrow.utcnow().to(timezone)
        self.save()

    def __str__(self):
        return self.title
