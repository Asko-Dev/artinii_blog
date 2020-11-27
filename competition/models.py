from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse



def validate_file_extension(value):
    if not value.name.lower().endswith('.pdf'):
        raise ValidationError(u'Please upload a PDF file')


class AmateurCompetition(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now=True)
    link = models.URLField(help_text='Format: https://www.yourmovielink.com', unique=True, blank=False)
    plot = models.TextField(max_length=500, help_text='500 characters')
    poster = models.ImageField(upload_to='competition_posters')
    letter = models.FileField(blank=True, upload_to='competition_letters', validators=[
                              validate_file_extension])

    def __str__(self):
        return f'{self.title} by {self.user.username}'

    # def save(self):
    #     img = Image.open(self.poster.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.poster.path)
    #
    #     super().save()

    def get_absolute_url(self):
        return reverse('competition-detail', kwargs={'pk': self.pk})
