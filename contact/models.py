from django.db import models

# Create your models here.
class Messages(models.Model):
    name = models.CharField(max_length=225, verbose_name="Your Name")
    phone = models.CharField(max_length=225, verbose_name="Your Email")
    message = models.TextField(verbose_name="Message")

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.name