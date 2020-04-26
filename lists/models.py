from django.db import models
from django.db import models
class Userinfo(models.Model):
    #objects = None
    objects = None
    name = models.TextField(max_length=200, blank=True)
    # term1 = models.ManyToManyField('Term1')
    # term2 = models.ManyToManyField('Term2')
    # term3 = models.ManyToManyField('Term3')
    # term4 = models.ManyToManyField('Term4')
    # term5 = models.ManyToManyField('Term5')
    # term6 = models.ManyToManyField('Term6')
    # term7 = models.ManyToManyField('Term7')
    # term8 = models.ManyToManyField('Term8')
    # gpa = models.ManyToManyField('GPA')
    #password = models.TextField(max_length=200, blank=True)
    def __str__(self):
        return self.name
class Term(models.Model):
    term = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    # GPA = models.CharField(max_length=255)
# class Term1(models.Model):
#     subject = models.CharField(max_length=255)
#     unit = models.CharField(max_length=255)
#     Grade = models.CharField(max_length=255)
#     GPA = models.CharField(max_length=255)
# class Term2(models.Model):
#     subject = models.CharField(max_length=255)
#     unit = models.CharField(max_length=255)
#     Grade = models.CharField(max_length=255)
#     GPA = models.CharField(max_length=255)
# class Term3(models.Model):
#     subject = models.CharField(max_length=255)
#     unit = models.CharField(max_length=255)
#     Grade = models.CharField(max_length=255)
#     GPA = models.CharField(max_length=255)
# class Term4(models.Model):
#     subject = models.CharField(max_length=255)
#     unit = models.CharField(max_length=255)
#     Grade = models.CharField(max_length=255)
#     GPA = models.CharField(max_length=255)
# class Term5(models.Model):
#     subject = models.CharField(max_length=255)
#     unit = models.CharField(max_length=255)
#     Grade = models.CharField(max_length=255)
#     GPA = models.CharField(max_length=255)
# class Term6(models.Model):
#     subject = models.CharField(max_length=255)
#     unit = models.CharField(max_length=255)
#     Grade = models.CharField(max_length=255)
#     GPA = models.CharField(max_length=255)
# class Term7(models.Model):
#     subject = models.CharField(max_length=255)
#     unit = models.CharField(max_length=255)
#     Grade = models.CharField(max_length=255)
#     GPA = models.CharField(max_length=255)
# class Term8(models.Model):
#     subject = models.CharField(max_length=255)
#     unit = models.CharField(max_length=255)
#     Grade = models.CharField(max_length=255)
#     GPA = models.CharField(max_length=255)
class GPA(models.Model):
    GPA_1 = models.CharField(max_length=255)
    GPA_2 = models.CharField(max_length=255)
    GPA_3 = models.CharField(max_length=255)
    GPA_4 = models.CharField(max_length=255)
    GPA_5 = models.CharField(max_length=255)
    GPA_6 = models.CharField(max_length=255)
    GPA_7 = models.CharField(max_length=255)
    GPA_8 = models.CharField(max_length=255)
