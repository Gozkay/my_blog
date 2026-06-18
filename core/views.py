from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from core.models import Article, Category, Comment, User


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
    category_post = Article.objects.filter(category=category)



    context = {
        'category': category,
        'categories': Categories,
        'category_post': category_post
    }

    return render(request, 'category_detail.html', context)
def post(request, slug):
    article = get_object_or_404(Article, slug=slug)
    categories = Category.objects.all()
    comments = Comment.objects.filter(article=article)

    context = {
        'article': article,
        'categories': categories,
        'comments': comments
    }
    

    return render(request, 'post_detail.html', context)
def add_comment(request, slug):
    article = Article.objects.get(slug=slug)
    if request.method == 'POST':
        body = request.POST.get('body')
        comment = Comment.objects.create(user=request.user, article=article, body=body)
        comment.save()
    return render(request, 'post_detail.html', {'article': article})
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')  # Redirect to the login page after successful registration
    return render(request, 'register.html') 
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout
