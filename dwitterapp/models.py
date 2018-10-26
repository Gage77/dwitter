from django.db import models
from django.urls import reverse
from django.utils import timezone
import arrow
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


class Comment(models.Model):
    post = models.ForeignKey('dwitterapp.Post', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    comment_date = models.DateTimeField(
        default=timezone.now)

    def comment_on_post(self):
        self.comment_date = arrow.utcnow().to(timezone)
        self.save()

    def __str__(self):
        return self.text
