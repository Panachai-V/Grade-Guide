from django.db import models
from django.db import models
class Userinfo(models.Model):
    objects = None
    name = models.TextField(max_length=200, blank=True)
    def __str__(self):
        return self.name

class Term(models.Model):
    term = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)

class GPA(models.Model):
    GPA_1 = models.CharField(max_length=255)
    GPA_2 = models.CharField(max_length=255)
    GPA_3 = models.CharField(max_length=255)
    GPA_4 = models.CharField(max_length=255)
    GPA_5 = models.CharField(max_length=255)
    GPA_6 = models.CharField(max_length=255)
    GPA_7 = models.CharField(max_length=255)
    GPA_8 = models.CharField(max_length=255)
