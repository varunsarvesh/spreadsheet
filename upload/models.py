from django.contrib.postgres.fields import ArrayField
from django.db import models


class avengers(models.Model):
    name = models.CharField(max_length=200)
    power = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class sheet(models.Model):
    file_name = models.CharField(max_length=200)
    header = ArrayField(models.CharField(max_length=110))
    details = ArrayField(ArrayField(models.CharField(max_length=110)))

    def __str__(self):
        return self.file_name