# Generated by Django 4.0.2 on 2022-03-01 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/images/blog-img.jpg/', upload_to='blog/images/'),
        ),
    ]
