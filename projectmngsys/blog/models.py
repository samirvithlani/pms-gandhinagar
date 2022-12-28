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

class Account(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    no = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'account'    
    
    def __str__(self):
        return self.name        
             

class User(Account):
    uname = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()         
    
    
    class Meta:
        db_table = 'user'
        
    def __str__(self):
        return self.name        
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    class Meta:
        db_table = 'author'
        
    def __str__(self):
        return self.name
    

class Books(models.Model):
    author  = models.ForeignKey(Author,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    
    class Meta:
        db_table = 'books'
        
    def __str__(self):
        return self.name                
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'product'

class Cart(models.Model):
    product = models.ManyToManyField(Product)
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'cart'
        
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.question_text
    
    class Meta:
        db_table = 'question'
        
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
    class Meta:
        db_table = 'choice'                