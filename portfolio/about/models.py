from django.db import models

# Create your models here.


class About(models.Model):
    subject = models.TextField()

    def __str__(self):
        return 'About'

    class Meta:
        verbose_name_plural = 'About'