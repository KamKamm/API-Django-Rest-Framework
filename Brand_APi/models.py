
# Brand_Api/models.py

from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')
    primary_colors = models.TextField()
    secondary_colors = models.TextField()
    font_family = models.CharField(max_length=100)
    mission = models.TextField()
    vision = models.TextField()

    def __str__(self):
        return self.name
