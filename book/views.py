from django.shortcuts import render
from .models import Book,Author,review

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request,'book/book_list.html',{'books':books})

