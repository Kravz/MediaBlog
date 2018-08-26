from django.views.generic.list import MultipleObjectMixin
from .models import Category, Article


class CategoryandArticlesListMixin(MultipleObjectMixin):

    def get_context_data(self, *args, **kwargs):
        context = {}
        context['categories'] = Category.objects.all()
        context['tab_articles'] = Article.objects.all()
        return context