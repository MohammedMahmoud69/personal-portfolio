from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    subject = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.email