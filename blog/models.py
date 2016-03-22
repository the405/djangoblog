from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Defines the blog's author table
class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

# Defines the blog's tag table
class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    tag_desc = models.CharField('Tag description',max_length=255)

    def __str__(self):
        return self.tag_name

# Defines the blog's post table
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

