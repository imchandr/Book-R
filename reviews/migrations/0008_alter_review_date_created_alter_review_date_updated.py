# Generated by Django 4.0.2 on 2022-02-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_alter_review_author_alter_review_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
