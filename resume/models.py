from django.db import models

# Create your models here
class Education(models.Model):
    years = models.CharField(max_length=20, verbose_name="Yili")
    topic = models.CharField(max_length=255, verbose_name="Mavzusi")
    desc = models.CharField(max_length=255, verbose_name="Mavzu haqida")

    class Meta:
        # verbose_name = 'Education'
        verbose_name_plural = 'Education'

    def __str__(self):
        return self.topic


class Experience(models.Model):
    years = models.CharField(max_length=20, verbose_name="Yili")
    name = models.CharField(max_length=255, verbose_name="Mavzusi")
    desc = models.CharField(max_length=255, verbose_name="Mavzu haqida")

    class Meta:
        # verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return self.name


class Awards(models.Model):
    years = models.CharField(max_length=20, verbose_name="Yili")
    name = models.CharField(max_length=255, verbose_name="Mukofot")
    where = models.CharField(max_length=255, verbose_name="Mukofot haqida", null=True)

    class Meta:
        verbose_name = 'Award'
        verbose_name_plural = 'Awards'

    def __str__(self):
        return self.name
