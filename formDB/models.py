from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=112)
    mobile = models.IntegerField()
    email = models.EmailField(unique=True)
    message = models.TextField()

    def __str__(self):
        return self.name
