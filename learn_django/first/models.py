from django.db import models


class Sites(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
