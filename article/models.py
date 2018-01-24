from django.db import models


class Article(models.Model):
    title = models.CharField(verbose_name='Titre', max_length=50)
    content = models.TextField(verbose_name='Contenu')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['title']

    def __str__(self):
        return self.title
