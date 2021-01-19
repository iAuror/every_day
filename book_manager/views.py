from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from book_manager.models import Book, BooksLike, Comment, CommentLike


class BookManager(View):
    def get(self, request):
        context = {
            'book': Book.objects.all().prefetch_related('author', 'owner'),
            'comment': Comment.objects.all().select_related('author')
        }
        return render(request, 'book_manager/index.html', context=context)


class AddBookLike(View):
    def get(self,request,id):
        if request.user.is_authenticated:
            BooksLike.objects.create(user=request.user, book_id=id)
            return redirect ('book-index')

class AddCommentLike(View):
    def get(self,request,id):
        if request.user.is_authenticated:
            CommentLike.objects.create(user=request.user, comment_id=id)
            return redirect('book-index')