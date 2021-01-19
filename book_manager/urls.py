from django.urls import path

from book_manager.views import BookManager, AddBookLike, AddCommentLike

urlpatterns = [
    path ('', BookManager.as_view(), name='book-index'),
    path ('add_book_like/<int:id>/', AddBookLike.as_view(), name = 'add-book-like'),
    path ('add_comment_like/<int:id>', AddCommentLike.as_view(), name= 'add-comment-like'),
]