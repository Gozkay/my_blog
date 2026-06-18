from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles/images')
    date_posted = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwrgs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwrgs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title} by {self.author}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on article {self.article} by {self.user}"