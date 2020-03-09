"""webproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogapp.views import homeview, addarticleview, getarticles, updatearticleview, articleview, registrationview, loginview, logoutview, deletearticle
from blogapi.views import testview, getarticles, createarticle, createuserview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', getarticles, name="get_article"),
    path('addarticle', addarticleview, name='add_article'),
    path('updatearticle/<int:id>/', updatearticleview, name="update_article"),
    path('article/<int:id>/', articleview, name="get_article" ),
    path('articledelete/<int:id>', deletearticle, name="delete_article"),
    path('registration', registrationview, name="user_registration"),
    path('login/', loginview, name="login"),
    path('logout', logoutview, name="logout"),
    path('api/v1/testview', testview),
    path('api/v1/articles/', getarticles),
    path('api/v1/creatarticle', createarticle ),
    path('api/v1/registration', createuserview )
]
