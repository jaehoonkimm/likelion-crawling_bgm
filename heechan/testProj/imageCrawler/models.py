from django.db import models

class ImageData(models.Model):
    image_link = models.URLField()