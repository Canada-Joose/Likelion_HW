from django.shortcuts import render, redirect
from .models import Article
# Create your views here.


def new(request):
    if request.method == 'POST':
        # POST 요청으로 온 데이터 확인
        print(request.POST)  # 이건 그냥 확인용으로 프린트하는 것
        new_article = Article.objects.create(
            title=request.POST['title'],
            category=request.POST['category'],
            content=request.POST['content'],
        )
        return redirect('list')  # list라는 이름의 글 목록이 있는 페이지로 보내라

    return render(request, 'new.html')


def list(request):
    articles = Article.objects.all()
    hobby_count = Article.objects.filter(category='hobby').count()
    food_count = Article.objects.filter(category='food').count()
    programming_count = Article.objects.filter(category='programming').count()
    return render(request, 'list.html', {'articles': articles, 'hobby_count': hobby_count, 'food_count': food_count, 'programming_count': programming_count})


def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'detail.html', {'article': article})


def blog(request):
    articles = Article.objects.all()
    hobby_count = Article.objects.filter(category='hobby').count()
    food_count = Article.objects.filter(category='food').count()
    programming_count = Article.objects.filter(category='programming').count()

    categories = Article.objects.all().values_list('category', flat=True).distinct()

    # hobby_art = 'hobby'
    # food_art = Article.objects.filter(category='food')
    # programming_art = Article.objects.filter(category='programming')
    return render(request, 'blog.html', {'hobby_count': hobby_count, 'food_count': food_count, 'programming_count': programming_count, 'categories': categories})


def category(request, category):
    articles = Article.objects.filter(category=category)
    # hobby_art = Article.objects.filter(category='hobby')
    # food_art = Article.objects.filter(category='food')
    # programming_art = Article.objects.filter(category='programming')
    return render(request, 'category.html', {'articles': articles, 'category': category
                                             # 'hobby_art': hobby_art, 'food_art': food_art, 'programming_art': programming_art
                                             })


# def category_food(request):
#     articles = Article.objects.all()
#     hobby_art = Article.objects.filter(category='hobby')
#     food_art = Article.objects.filter(category='food')
#     programming_art = Article.objects.filter(category='programming')
#     return render(request, 'category.html', {'articles': articles, 'hobby_art': hobby_art, 'food_art': food_art, 'programming_art': programming_art})


# def category_programming(request):
#     articles = Article.objects.all()
#     hobby_art = Article.objects.filter(category='hobby')
#     food_art = Article.objects.filter(category='food')
#     programming_art = Article.objects.filter(category='programming')
#     return render(request, 'category.html', {'articles': articles, 'hobby_art': hobby_art, 'food_art': food_art, 'programming_art': programming_art})
