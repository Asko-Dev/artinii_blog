from multiselectfield import MultiSelectField
from django import forms
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaulttags import register
from django.template.defaultfilters import slugify


class Post(models.Model):
    OUR_MISSION = "our_mission"
    FILM_MARKETPLACE = "film_marketplace"
    PUBLIC_SCREENINGS = "public_screenings"
    CONTENT_DELIVERY = "content_delivery"

    template_helper = {
        OUR_MISSION: "Our Mission",
        FILM_MARKETPLACE: "Film Marketplace",
        PUBLIC_SCREENINGS: "Public Screenings",
        CONTENT_DELIVERY: "Content Delivery",
    }

    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"

    TAG_CHOICES = [
        (OUR_MISSION, "Our Mission"),
        (FILM_MARKETPLACE, "Film Marketplace"),
        (PUBLIC_SCREENINGS, "Public Screenings"),
        (CONTENT_DELIVERY, "Content Delivery"),
        ]

    STATUS_CHOICES = [("ACTIVE", "Active"), ("DISABLED", "Disabled")]

    main_title = models.CharField(max_length=100, default=" ", blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    title = models.CharField(max_length=100, default=" ", blank=True)
    content = models.TextField(default=" ", blank=True)
    image = models.ImageField(upload_to='blog_pics', blank=True, null=True)
    title2 = models.CharField(max_length=100, default=" ", blank=True)
    content2 = models.TextField(default=" ", blank=True)
    image2 = models.ImageField(upload_to='blog_pics', blank=True, null=True)
    title3 = models.CharField(max_length=100, default=" ", blank=True)
    content3 = models.TextField(default=" ", blank=True)
    image3 = models.ImageField(upload_to='blog_pics', blank=True, null=True)
    title4 = models.CharField(max_length=100, default=" ", blank=True)
    content4 = models.TextField(default=" ", blank=True)
    image4 = models.ImageField(upload_to='blog_pics', blank=True, null=True)
    title5 = models.CharField(max_length=100, default=" ", blank=True)
    content5 = models.TextField(default=" ", blank=True)
    image5 = models.ImageField(upload_to='blog_pics', blank=True, null=True)
    socials_title = models.CharField(max_length=100, default=" ", blank=True)
    socials_pitch = models.TextField(default=" ", blank=True)
    name_link = models.CharField(max_length=100, default=" ", blank=True)
    link = models.URLField(default=" ", blank=True)
    name_link2 = models.CharField(max_length=100, default=" ", blank=True)
    link2 = models.URLField(default=" ", blank=True)
    name_link3 = models.CharField(max_length=100, default=" ", blank=True)
    link3 = models.URLField(default=" ", blank=True)
    tag = MultiSelectField(max_length=200, choices=TAG_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ACTIVE)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.main_title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.main_title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)
