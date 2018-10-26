from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=140)
    create_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField('date published', default=timezone.now)
    attachment = models.FileField(upload_to='documents/', blank=True, null=True)

    class Meta:
        ordering = ['-published_date']

    def get_absolute_url(self):
        return reverse('post', self.pk)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def was_published_recently(self):
        return self.published_date >= timezone.now() - datetime.timedelta(days=1)

    def __unicode__(self):
        return self.title