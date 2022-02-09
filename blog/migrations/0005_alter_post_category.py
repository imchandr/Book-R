# Generated by Django 4.0.2 on 2022-02-08 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, default='dango', null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category'),
        ),
    ]
