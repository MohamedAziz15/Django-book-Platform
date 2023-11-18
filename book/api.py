from .serilizer import bookSerlizer
from .models import Book,Author,review
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def book_list_api(request):
    books = Book.objects.all()
    data = bookSerlizer(books,many=True).data
    return Response({"message":"success","status":200,"Books":data})


@api_view(['GET'])
def book_detail_api(request,id):
    book = Book.objects.get(id=id)
    data = bookSerlizer(book,many=True).data
    return Response({"message":"success","status":200,"Book":data})






