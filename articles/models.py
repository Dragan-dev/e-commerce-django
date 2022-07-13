from django.db.models.signals import pre_save, post_save
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
import random


class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True,blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateField(
        auto_now=False, auto_now_add=False, default=timezone.now, blank=True, null=True)

    def save(self, *args, **kwargs):
        # if self.slug is None:
        # self.slug=slugify(self.title)
        super().save(*args, **kwargs)




def slugify_instance_title(instance, save=False, new_slug=None):
        if new_slug is not None:
            slug = new_slug
        else:
            slug = slugify(instance.title)

        qs = Article.objects.filter(slug=slug).exclude(id=instance.id)

        if qs.exists:
            rand_int = random.randint(100, 300)
            slug = f"{slug}-{rand_int}"

        instance.slug = slug
        if save:
            instance.save()
        return instance


def article_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')
    print(sender, instance)
    if instance.slug is None:
        slugify_instance_title(instance, save=False,)


pre_save.connect(article_pre_save, sender=Article)


def article_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(article_post_save, sender=Article)
