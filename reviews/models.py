from django.db import models
from django.contrib import auth


class Publisher(models.Model):
    '''holds information about the book publisher'''

    name = models.CharField(max_length=50, help_text="name of the publisher.")
    website = models.URLField(help_text="Publishers website")
    email = models.EmailField(help_text="Publisher's email address")

    def __str__(self):
        return self.name


class Book(models.Model):
    '''Contains information about the book'''

    title = models.CharField(max_length=50, verbose_name="title of the book")
    publication_date = models.DateField(
        verbose_name='Date when the book was published')
    isbn = models.CharField(
        max_length=20, verbose_name='ISBN number of the book')
    publisher_name = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors_name = models.ManyToManyField(
        'Contributor', through='BookContributor')
    '''this BookContributor field results an aditional table named BookContributor combined wth book and Contributor tables as foreign key'''

    def __str__(self):
        return self.title


class Contributor(models.Model):
    '''Contains information about the book contributor's e.g. author, co-author, editor, etc'''

    first_name = models.CharField(
        max_length=50, help_text="First name of the contributor")
    last_name = models.CharField(
        max_length=50, help_text="Last name of the contributor")
    email = models.EmailField(help_text="Email address of the contributor")

    def __str__(self):
        return self.first_name


class BookContributor(models.Model):
    '''created this model for m2m field named contributor_name in books model for contribution role in the book model'''
    class ContributionRole(models.TextChoices):
        AUTHOR = 'AUTHOR', 'Author'
        CO_AUTHOR = 'CO_AUTHOR', 'Co-Author'
        EDITOR = 'EDITOR', 'Editor'

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name='The Role of Contributer in the book',
                            choices=ContributionRole.choices, max_length=20)


class Review(models.Model):
    content = models.TextField(help_text='the review text', max_length=255)
    rating = models.IntegerField(help_text='rating the reviewer has giver')
    date_created = models.DateTimeField(
        auto_now_add=True, help_text='date and time when the review was created')
    date_edited = models.DateTimeField(
        null=True, help_text='date and time when the review was edited')
    created_by = models.ForeignKey(
        auth.get_user_model(), on_delete=models.CASCADE)
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE)
