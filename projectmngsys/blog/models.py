from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    isActive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rollno = models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'student'
         