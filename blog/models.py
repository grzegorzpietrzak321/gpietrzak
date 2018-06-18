from django.db import models
from django.contrib.auth.models import *


ARTICLE_STATUS = (
    ('P', 'Published'),
    ('D', 'Draft'),

)


class Article(models.Model):
    title = models.CharField('Article title', max_length=300)
    slug = models.CharField('Article link', max_length=100, unique=True)
    content = models.TextField('Article content')
    posted_date = models.DateTimeField('Posted date', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    article_status = models.CharField('Article status', max_length=1, choices=ARTICLE_STATUS, default='D')
    # tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return "{0} posted by {1}".format(self.title, self.author.username)


class Category(models.Model):
    name = models.CharField('Category name', max_length=100)
    slug = models.CharField('Category link', max_length=100, unique=True)
    # icon = models.ImageField('Category icon', upload_to='icons', blank=True)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    tag = models.CharField('Tag', max_length=100)

    def __unicode__(self):
        return self.tag
