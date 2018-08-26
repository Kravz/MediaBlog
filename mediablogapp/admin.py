from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.filters import ListFilter
from .models import Category, Article, Comment, UserAccount


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(UserAccount)


