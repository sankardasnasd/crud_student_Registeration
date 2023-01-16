from django.db import models

# Create your models here.

class Students(models.Model):
    student_name = models.CharField(max_length=200)
    student_address = models.CharField(max_length=1000)
    student_phone = models.BigIntegerField()

    def __str__(self):
        return self.student_name
