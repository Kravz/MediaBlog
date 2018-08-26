from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


class Category(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})


def generate_filename(instance, filename):
    filename = instance.slug + '.jpg'
    return "{0}/{1}".format(instance.slug, filename)


class Article(models.Model):

    category = models.ForeignKey(Category)
    title = models.CharField(max_length=1000)
    slug = models.SlugField()
    image = models.ImageField(upload_to=generate_filename)
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    comments = GenericRelation('Comment')
    users_reaction = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return "Статья '{0}' из категории '{1}'".format(self.title, self.category.name)

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'category': self.category.slug, 'slug': self.slug})


class Comment(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    comment = models.TextField(verbose_name='Комментарий')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Время поста')

    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, verbose_name='Контент')
    object_id = models.PositiveIntegerField(verbose_name='ID контента')
    content_object = GenericForeignKey('content_type', 'object_id')


class UserAccount(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    favorite_articles = models.ManyToManyField(Article)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('account_view', kwargs={'user': self.user.username})

