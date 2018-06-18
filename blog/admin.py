from django.contrib import admin

# Register your models here.

from .models import Article, Category


@admin.register(Article)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'posted_date', 'article_status')
    list_editable = ('title', 'article_status')


admin.site.register(Category)
