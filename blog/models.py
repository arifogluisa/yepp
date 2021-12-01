from django.db import models
from django.utils import timezone
from django.urls import reverse
from users.models import Profile


class Post(models.Model):
    content = models.TextField(verbose_name='Məzmun')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.content)[:30]

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('-date_posted',)
