from django.shortcuts import render
from .forms import ArticleForm
from django.contrib import messages

# Create your views here.
def homeview(request):
    return render(request, 'home.html')


def addarticleview(request):
    if request.method == "POST":
        print('POST method triggered')
        form = ArticleForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
        messages.success(request, "New article added successfully")
        form = ArticleForm()
        return render(request, 'addarticle.html', {"form":form} )
    else:
        form = ArticleForm()
        return render(request, 'addarticle.html', {"form":form})
    
