from django.db import models

# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    icon = models.ImageField(upload_to='media/services')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Services'