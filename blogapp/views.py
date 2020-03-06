from django.shortcuts import render, redirect
from .forms import ArticleForm
from django.contrib import messages
from .models import Article

# Create your views here.
def homeview(request):
    return render(request, 'home.html')


def addarticleview(request):
    if request.method == "GET":
        form = ArticleForm()
        return render(request, 'addarticle.html', {"form":form})
    if request.method == "POST":
        print("POST Method triggered")
        form = ArticleForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, "Article added successfully")
        return redirect('/')


def getarticles(request):
    articles = Article.objects.all().order_by('-posted_on')
    print(articles)
    return render(request, 'home.html', {'articles':articles})


def updatearticleview(request, id):
    if request.method == "GET":
        print(id)
        article = Article.objects.get(id=id)
        form = ArticleForm(initial={'title':article.title, 'content':article.content})
        return render(request, 'update_article.html', {'form':form})
    if request.method == "POST":
        print(id)
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = Article.objects.get(id=id)
            title = request.POST.get('title')
            content = request.POST.get('content')
            article.title = title
            article.content = content
            article.save()
        return redirect('/')








    # if request.method == "POST":
    #     print('POST method triggered')
    #     form = ArticleForm(request.POST)
    #     print(form.is_valid())
    #     if form.is_valid():
    #         form.save()
    #     messages.success(request, "New article added successfully")
    #     form = ArticleForm()
    #     return render(request, 'addarticle.html', {"form":form} )
    # else:
    #     form = ArticleForm()
    #     return render(request, 'addarticle.html', {"form":form})
    
