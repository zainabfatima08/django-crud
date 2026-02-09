from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Student Name")
    email = models.EmailField(unique=True, verbose_name="Email Address")
    course = models.CharField(max_length=100, verbose_name="Course", default='Not Specified')
    age = models.IntegerField(verbose_name="Age")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        ordering = ['-id']
        verbose_name = "Student"
        verbose_name_plural = "Students"
    
    def __str__(self):
        return f"{self.name} - {self.course}"








