from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Publisher(models.Model):
    '''holds information about the book publisher'''

    name = models.CharField(max_length=50, help_text="name of the publisher.")
    website = models.URLField(help_text="Publishers website")
    email = models.EmailField(help_text="Publisher's email address")

    def __str__(self):
        return self.name


class Book(models.Model):
    '''Contains information about the book'''
    BOOK_TYPE_CHOICES = (
        ('printbook', 'PrintBook'),
        ('ebook', 'Ebook'),
    )
    BOOK_LANGUAGE_CHOICES = (
        ('hindi', 'Hindi'),
        ('english', 'English'),
    )

    title = models.CharField(max_length=50, verbose_name="title of the book")
    publication_date = models.DateField(
        verbose_name='Date when the book was published')
    isbn = models.CharField(
        max_length=20, verbose_name='ISBN number of the book')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(
        'Contributor', through='BookContributor',)
    
    image = models.ImageField(
        upload_to='review/images/', default='book_default.jpg', blank=True, null=True)
    type = models.CharField(max_length=20, choices=BOOK_TYPE_CHOICES,
                            default='printbook', blank=True, null=True)
    language = models.CharField(
        max_length=20, choices=BOOK_LANGUAGE_CHOICES, default='english', blank=True, null=True)
    genre = models.CharField(max_length=255,blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    price = models.IntegerField(default=499, blank=True, null=True)
    stock = models.IntegerField(default=10)

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

    def __str__(self):
        return str(self.book)


class Review(models.Model):
    book = models.ForeignKey(
        Book, related_name='review', on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, related_name='review_author', blank=True, null=True, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],default=5)
    date_created = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.content
    

