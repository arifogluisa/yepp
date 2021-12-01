from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='following', blank=True)
    bio = models.TextField(default='no bio...')
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')


    def profile_post(self):
        return self.post_set.all()

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        ordering = ('-created',)

"""
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # saving image first

        img = Image.open(self.image.path)  # Open image using self

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.image.path)  # saving image at the same path
"""