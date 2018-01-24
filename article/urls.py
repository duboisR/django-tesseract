from django.urls import path

import article.views


urlpatterns = [
    path('api/article/tesseract/', article.views.TesseractView.as_view()),
]
