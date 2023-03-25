from django.db import models

class CourseModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True,default="This is the descritpion of the Course")
    hours = models.PositiveSmallIntegerField(blank=True, null=True,default=10)

def __str__(self):
    return self.title
