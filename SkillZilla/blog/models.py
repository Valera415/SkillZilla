from django.db import models


class Comment(models.Model):
    author = models.CharField(max_length=15, blank=False)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author

    class Meta:
        ordering = ['-created_at']


class Project(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=250)
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)
    photo = models.ImageField(upload_to='photos/')
    template_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
