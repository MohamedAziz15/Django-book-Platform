from collections.abc import Iterable
from django.db import models
# from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    biography = models.TextField(max_length=1000)
    slug = models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.name 
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        return super(Author,self).save(*args, **kwargs)
    
    #  class class Meta:
    #     db_table = ''
    #     managed = True
    #     verbose_name = 'ModelName'
    #     verbose_name_plural = 'ModelNames'


class Book(models.Model):
    title = models.CharField(max_length=50)
    Author = models.ForeignKey('Author',on_delete=models.SET_NULL,related_name="author_book", null=True, blank=True)
    publish_date = models.DateField()
    price = models.FloatField()
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.title 
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        return super(Book ,self).save(*args, **kwargs)
    

class review(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='Book_reviews')
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[
            MinValueValidator(1, message="Value must be greater than or equal to 1."),
            MaxValueValidator(5, message="Value must be less than or equal to 5."),
        ])
    content = models.TextField(max_length=2000)


