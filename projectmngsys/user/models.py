from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    #mobile for studnet
    #teacher degree
    
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    mobile = models.CharField(max_length=10,null=True,blank=True)
    
    class Meta:
        db_table = 'student1'

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    
    class Meta:
        db_table = 'teacher1'            
