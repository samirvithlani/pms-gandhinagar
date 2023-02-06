from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    mobile = models.CharField(max_length=10,null=True,blank=True)
    degree = models.CharField(max_length=100,null=True,blank=True)
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


class Eletronics(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
    
    class Meta:
        db_table = 'eletronics1'
    
    @property
    def imageURL(self):
        try:
            url = self.file.url
        except:
            url = ''
        return url
    