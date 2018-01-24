from django.contrib import admin

import article.models


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_content')

    def get_content(self, obj):
        return obj.content[:50]
    get_content.short_description = 'Extrait du contenu'


admin.site.register(article.models.Article, ArticleAdmin)
