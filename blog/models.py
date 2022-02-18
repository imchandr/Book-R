from distutils.command.upload import upload
from email.policy import default
from enum import unique
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
import readtime
from ckeditor.fields import RichTextField

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    image = models.ImageField(upload_to='blog/images/', default='blog/images/blog-img.jpg/')
    # category = models.ForeignKey(Category, null=True,default='dango', blank=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = RichTextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default = 'draft')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    
    class Meta:
        ordering = ('-publish',)
        
        

    def save(self):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save()
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.slug])
    def get_readtime(self):
        result = readtime.of_text(self.body)
        return result.text

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentetor_name')
    # email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering =['created']

        def __str__(self):
            return f"commented by {{self.name}} on {{self.post}}"

