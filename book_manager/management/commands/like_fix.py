from django.core.management.base import BaseCommand
from django.db.models import Count
from book_manager.models import Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        book = Book.objects.annotate(count_like=Count('user_like'))
        # Book.objects.bulk_update(like=Count('user_like'))
        for b in book:
            b.like = b.count_like
        Book.objects.bulk_update(book, ['like'])
