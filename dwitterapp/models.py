import arrow
from django.core.urlresolvers import reverse
from django.db import models
from cuser.fields import CurrentUserField


class Post(models.Model):
    author = CurrentUserField(related_name='%(app_label)s_%(class)s_author', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=140)
    create_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)
    attachment = models.FileField(upload_to='documents/', blank=True, null=True)

    class Meta:
        ordering = ['-published_date']

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def publish(self):
        self.published_date = arrow.now()
        self.save()

    def was_published_recently(self):
        return self.published_date >= arrow.now().shift(days=-1).datetime

    def __unicode__(self):
        return self.title
