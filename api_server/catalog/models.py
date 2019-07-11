from django.db import models

class Task(models.Model):
    text = models.TextField()

    class Meta:
        app_label = 'catalog'

