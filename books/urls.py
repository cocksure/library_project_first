from django.urls import path
from .views import BookListapiView, BookDetailApiView,\
    BookUpdatedeleteApiView, BookListCreateApiView, BookCreateView, \
    BookDeleteApiView, BookUpdateApiView, BookViewset

from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('books', BookViewset, basename='books')


urlpatterns = [
    # path('books/', BookListapiView.as_view()),
    # path('books/create/', BookCreateView.as_view()),
    # path('books/<int:pk>/detail/', BookDetailApiView.as_view()),
    # path('bookupdatedelete/<int:pk>/', BookUpdatedeleteApiView.as_view()),
    # path('booklistcreate/', BookListCreateApiView.as_view()),
    # path('books/<int:pk>/delete', BookDeleteApiView.as_view()),
    # path('books/<int:pk>/update', BookUpdateApiView.as_view())
]


urlpatterns += router.urls