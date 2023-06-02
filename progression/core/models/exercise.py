from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField(max_length=1023, blank=True)
    # FEAT Add more media fields for better description
