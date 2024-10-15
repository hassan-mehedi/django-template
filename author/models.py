from django.db import models

# Create your models here.
class Author(models.Model):
    genders = {
        'MALE': 'MALE',
        'FEMALE': 'FEMALE',
        'OTHER': 'OTHER',
    }
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.TextField()
    image = models.ImageField(upload_to='author')
    gender = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)