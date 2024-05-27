from django.contrib import admin
from .models import Category, Author, PostCategory, Post, Comment

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(PostCategory)
admin.site.register(Post)

