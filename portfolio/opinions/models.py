from django.db import models

# Create your models here.

class Opinions(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    opinion = models.TextField(null=False, blank=False)
    personal_photo = models.ImageField(upload_to='media/opinions')
    date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Opinions'