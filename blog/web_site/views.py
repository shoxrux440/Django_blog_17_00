from django.shortcuts import render, HttpResponse
from .models import Article
# Create your views here.


def home_view(request):
    articles = Article.objects.all()
    context = {
        "articles": articles
    }
    return render(request, 'web_site/index.html', context)