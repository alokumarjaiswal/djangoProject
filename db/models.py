from django.db import models


# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    established_year = models.IntegerField()

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=150)
    dean = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='schools')

    def __str__(self):
        return f"{self.name} | {self.dean}"


class Program(models.Model):
    name = models.CharField(max_length=200)
    duration = models.IntegerField(help_text="in Years")
    fee = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='programs')

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField(help_text="in Years")
    roll_no = models.IntegerField()
    email = models.EmailField(unique=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name
