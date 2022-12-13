from django.test import TestCase
from django.urls import resolve, reverse

from app_blog.views import ArticleList, HomePageView


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, HomePageView)


class ArticlesTests(TestCase):
    def test_articles_view_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_articles_url_resolves_home_view(self):
        view = resolve('/articles')
        self.assertEquals(view.func.view_class, ArticleList)


class ArticlesByCategoryTests(TestCase):
    def test_view_status_code(self):
        url = reverse('articles-category-list', args=('name',))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
