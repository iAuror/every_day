# Generated by Django 3.1.5 on 2021-01-19 15:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_manager', '0002_book_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='like',
        ),
        migrations.AddField(
            model_name='book',
            name='like',
            field=models.ManyToManyField(related_name='liked_books', to=settings.AUTH_USER_MODEL),
        ),
    ]