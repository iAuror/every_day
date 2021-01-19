from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    title = models.CharField(max_length=100, verbose_name='Название ')
    text = models.TextField(verbose_name='Текст книги')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления', null=True)
    genre = models.ForeignKey('Genre', verbose_name='Жанр', null=True, on_delete=models.CASCADE)
    owner = models.ManyToManyField(User, verbose_name='Книгу добавил', related_name='user_books')
    author = models.ManyToManyField('Author', verbose_name='Автор книги', related_name='author_books')
    user_likes = models.ManyToManyField(User, through='book_manager.BooksLike', related_name='liked_books')
    like = models.PositiveIntegerField(verbose_name='Количество лайков', default=0)

    def __str__(self):
        return self.title


class BooksLike(models.Model):
    class Meta:
        unique_together = ('user', 'book')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_book')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='liked_by_user')

    # def save(self, **kwargs):
    #     try:
    #         super().save()
    #     except:
    #         BooksLike.objects.get(user=self.user, book=self.book).delete()

    def save(self, **kwargs):
        try:
            super().save()
        except:
            self.book.like -= 1
            BooksLike.objects.get(user=self.user, book=self.book).delete()
        else:
            self.book.like += 1
        self.book.save()


class Comment(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    text = models.TextField(verbose_name='Комментарий')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Время комментария')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    user_like = models.ManyToManyField(User, through='book_manager.CommentLike', related_name='liked_comments')
    likes = models.PositiveIntegerField(verbose_name='Количество лайков', default=0)


class CommentLike(models.Model):
    class Meta:
        unique_together = ('user', 'comment')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_comment')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='liked_by_user')

    def save(self, **kwargs):
        try:
            super().save()
        except:
            CommentLike.objects.get(user=self.user, comment=self.comment).delete()
            self.comment.likes -= 1
        else:
            self.comment.likes += 1
        self.comment.save()


class Genre(models.Model):
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    genre = models.CharField(max_length=50, verbose_name='Жанр книги')

    def __str__(self):
        return self.genre


class Author(models.Model):
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    author = models.CharField(max_length=100, verbose_name='Автор', )

    def __str__(self):
        return self.author
