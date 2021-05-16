from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('authors', views.authors),
    path('books/create', views.create_book),
    path('authors/create', views.create_author),
    path('authors/<int:author_id>', views.author_info),
    path('books/<int:book_id>', views.book_info),
    path('books/<int:book_id>/assign', views.assign_book),
    path('authors/<int:author_id/assign', views.assign_author)
]
