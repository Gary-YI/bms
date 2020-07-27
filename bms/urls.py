"""bms URL Configuration

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
from django.urls import path, include, re_path
from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #书籍页面
    re_path('^$', views.books, name='books'),
    #添加书籍
    re_path('add/', views.add, name='add'),
    #修改书籍
    re_path(r'edit/(\d+)', views.edit, name='edit'),
    #删除书籍
    re_path(r'delbook/(\d+)', views.delbook, name='delbook')

]
