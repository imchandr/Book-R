# Generated by Django 4.0.2 on 2022-02-10 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0004_rename_first_name_contributor_first_names_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['date_created']},
        ),
        migrations.RemoveField(
            model_name='review',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='review',
            name='date_edited',
        ),
        migrations.AddField(
            model_name='review',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, help_text='date and time when the review was edited'),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=5, help_text='rating the reviewer has giver'),
        ),
    ]
