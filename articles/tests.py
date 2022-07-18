from .utils import slugify
from django.test import TestCase

# Create your tests here.
from . models import Article


class ArticleTestCase(TestCase):

    def setUp(self):
        self.num_of_articles = 5
        for i in range(self.num_of_articles):
            Article.objects.create(
                title=' Testing case title', content='Testing case content')

    def test_qs_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())

    def test_qs_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(), self.num_of_articles)

    def test_hw_slug(self):
        obj = Article.objects.all().order_by("id").first()
        title = obj.title
        slug = obj.slug
        slugified_title = slugify(title)
        self.assertEqual(slug, slugified_title)

    def test_hw_slug(self):
        qs = Article.objects.exclude(slug__iexact__= 'hello world')
        for obj in qs:
            title = obj.title
            slug = obj.slug
            slugified_title = slugify(title)
            self.assertNotEquals(slug, slugified_title) 