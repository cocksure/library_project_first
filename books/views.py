from rest_framework import generics, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response

#
# class BookListapiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookListapiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        print(books)
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'status': f'Returned {len(books)} books',
            'books': serializer_data
        }

        return Response(data)


class BookDetailApiView(APIView):

    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_date = BookSerializer(book).data

            data = {
                'status': 'Successfull',
                'book': serializer_date
            },
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {'xolati': 'Does not exists',
                 'sms': 'Book id is not found'}, status=status.HTTP_404_NOT_FOUND
            )



# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookUpdatedeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            books = serializer.save()
            data = {'status': f" Books are saved to the database.",
                    'books': data
                    }
            return Response(data)
        else:
            return Response(
                {'status': False,
                 'message': 'serializer is not valid'}, status=status.HTTP_400_BAD_REQUEST
            )


class BookDeleteApiView(APIView):

    def delete(self, request, pk):
        try: #get_object_or_404 bosa try ecxeptlar keremss
            book = Book.objects.get(id=pk)
            book.delete()
            return Response({
                'status': True,
                'Message': 'Successfully deleted'
            })
        except Exception:
            return Response({
                'status': False,
                'message': 'Book si not found'
            })


class BookUpdateApiView(APIView):

    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer
        return Response(
            {
                'status': True,
                'message': f"Book updated successfully"

            }
        )


class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
