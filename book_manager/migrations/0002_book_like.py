# Generated by Django 3.1.5 on 2021-01-19 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='like',
            field=models.PositiveIntegerField(default=0, verbose_name='Лайк '),
        ),
    ]
