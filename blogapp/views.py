from django.shortcuts import render, redirect
from .forms import ArticleForm
from django.contrib import messages
from .models import Article

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login, logout

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



def articleview(request, id):
    if request.method == "GET":
        article = Article.objects.get(id=id)
        return render(request, 'article.html', {"article":article} )




def registrationview(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, 'registration.html', {"form":form})
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            username_status = User.objects.filter(username=username).exists()
            print(username_status, 'username status')
            if username_status == False:
                User.objects.create_user(username=username, password=password1)
                return redirect('/login')
            else:
                form = UserCreationForm()
                messages.error(request, "Username already taken.")
                return render(request, 'registration.html', {"form":form} )
        else:
            form = UserCreationForm()
            messages.error(request, "Both password are not Matching.")
            return render(request, 'registration.html', {"form":form} )


def loginview(request):
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, 'login.html', {"form":form})
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            password_status = check_password(password, user.password)
            print(password_status, "this is password status")
            if password_status == True:
                login(request, user)
                return redirect('/')
            else:
                form = AuthenticationForm()
                messages.error(request, "Login failed.")
                return render(request, 'login.html', {"form":form})
        except:
            form = AuthenticationForm()
            messages.error(request, "Username or Password Invalid.")
            return render(request, 'login.html', {"form":form})

def logoutview(request):
    logout(request)
    return redirect('/')


