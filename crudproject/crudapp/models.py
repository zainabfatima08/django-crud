from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 70)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
    
# CREATE Object

