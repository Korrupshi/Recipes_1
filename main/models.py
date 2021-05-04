from django.db import models
from autoslug import AutoSlugField
from django.shortcuts import reverse

# Create your models here.
# Model for Topics
class Topic(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title")

    def __str__(self):
        return self.title

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = AutoSlugField(populate_from="title")
    image = models.CharField(max_length=500)
    ingredients = models.TextField()
    directions = models.TextField()
    servings = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    calories = models.CharField(max_length=6)
    protein = models.CharField(max_length=6)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    link = models.URLField()

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("detail", kwargs={
            "slug":self.slug,
        })
