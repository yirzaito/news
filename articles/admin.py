from django.contrib import admin

# Register your models here.
from .models import Article, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline,]
    list_display =["title","body","author",]

admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)

