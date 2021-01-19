from django.contrib import admin

from book_manager.models import Book, Comment, Genre, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'genre')
    list_display_links = ('title',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('book', 'author')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author',)


admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Author, AuthorAdmin)
