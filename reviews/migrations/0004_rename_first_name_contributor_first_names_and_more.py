# Generated by Django 4.0 on 2021-12-27 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_rename_contributors_name_book_contributors_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contributor',
            old_name='first_name',
            new_name='first_names',
        ),
        migrations.RenameField(
            model_name='contributor',
            old_name='last_name',
            new_name='last_names',
        ),
    ]
