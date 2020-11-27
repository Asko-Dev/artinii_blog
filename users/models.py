from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from sorl.thumbnail import get_thumbnail


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #
    #     im = get_thumbnail(self.image.path, '300x300', crop='center', quality=99)
    #     img = Image.open(im)
    #     img.save(self.image.path)
