# Generated by Django 4.0.2 on 2022-02-10 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_alter_review_date_created_alter_review_date_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default='book_default.jpg', null=True, upload_to='review/images/'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(blank=True, choices=[('hindi', 'Hindi'), ('english', 'English')], default='english', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(blank=True, default=499, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='stock',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='book',
            name='type',
            field=models.CharField(blank=True, choices=[('printbook', 'PrintBook'), ('ebook', 'Ebook')], default='printbook', max_length=20, null=True),
        ),
    ]
