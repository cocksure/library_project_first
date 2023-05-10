from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'content', 'author', 'isbn', 'price')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('title', None)

        # check title if it contains only alphabetical chars
        if not title.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'message': 'E son yozma lotin harflaridan yoz'
                }
            )

        # check title and author from database existanse
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    'status': False,
                    'message': 'Kitob sarlavlahi bir xil bolishi keremasu'
                }
            )
        return data

    def validate_price(self, price):
        if price < 0 or price > 999999999:
            raise ValidationError(
                {
                    'status': False,
                    'message': 'E boladigan narx yozgin'
                }
            )
