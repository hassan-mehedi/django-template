from django.db import models

# Create your models here.
class Article(models.Model):
    article_categories = {
        'IT': 'IT',
        'SPORT': 'SPORT',
        'POLITICS': 'POLITICS',
        'OTHER': 'OTHER',
    }
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=10, choices=article_categories)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'article'
        constraints = [
            models.CheckConstraint(check=models.Q(category__in=['IT', 'SPORT', 'POLITICS', 'OTHER']), name='valid_category')
        ]