from django.db import models

class Student(models.Model):
    registration_number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    semester = models.IntegerField()
    sgpa = models.FloatField()
    cgpa = models.FloatField()
    def __str__(self):
        return f"{self.name} - {self.registration_number}"