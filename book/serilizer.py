from rest_framework import serializers
from .models import Author, Book, review

class bookSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


        







