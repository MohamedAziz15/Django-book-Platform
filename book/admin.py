from django.contrib import admin
from .models import Book,Author,review
from django_summernote.admin import SummernoteModelAdmin




class Bookadmin(SummernoteModelAdmin):
    list_display = ['title', 'Author', 'publish_date','price']
    search_fields = ['title']
    list_filter = ('title', 'Author', 'price')
    summernote_fields = '__all__'
    



# Register your models here.
admin.site.register(Book,Bookadmin)
admin.site.register(Author)
admin.site.register(review)

