from django.db import models

# Create your models here.



class School(models.Model):
    name=models.CharField(max_length=10)
    principal=models.CharField(max_length=10)


class Student(models.Model):
    school=models.ForeignKey(School,on_delete=models.CASCADE)
    sname=models.CharField(max_length=10)
    age=models.IntegerField()