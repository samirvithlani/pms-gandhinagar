from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    genere = models.CharField(max_length=100)
    
    class Meta:
        db_table = "post"
    
    def __str__(self):
        return self.title
                