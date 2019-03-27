from django.db import models

import django_tesseract.widgets


class Article(models.Model):
    title = models.CharField(verbose_name='Titre', max_length=50)
    content = django_tesseract.widgets.TesseractField(verbose_name='Contenu')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['title']

    def __str__(self):
        return self.title
