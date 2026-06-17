from django.shortcuts import render
from core.models import Article, Category, Comment


# Create your views here.
def home(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    comments = Comment.objects.all()

    context = {
        'articles': articles,
        'categories': categories,
        'comments': comments
    }

    return render(request, 'post_list.html', context)

def category(request,name):
    category = Category.objects.get(name=name)
    Categories = Category.objects.all()


    context = {
        'category': category,
        'categories': Categories
        
    }

    return render(request, 'category_detail.html', context)