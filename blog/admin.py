from django.contrib import admin
from blog.models import Post, Comment, Category

admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =("title","slug","author","publish", "status",)
    list_filter = ('status', 'created', 'publish', 'status')
    search_fields =('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish', )

@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("name", "post","created","updated", "active")
    list_filter = ("active","created","updated")
    search_fields = ('name',"body")






