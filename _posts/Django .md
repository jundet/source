---
title: Django 使用教程
date: 2019-01-29 11:19:53
tags: # WebAPI 
    - 前端开发
categories: 编程
---

## 示例1：安装Django并创建简单项目

详情见https://docs.djangoproject.com/zh-hans/2.1/intro/tutorial01/

环境基础为windows10+anaconda3

### 1、安装Django（版本2.1.5）

```shell
pip install Django==2.1.5
```

### 2、查看版本

```shell
python -m django --version
```

### 3、创建项目

```shell
django-admin startproject mysite
```

```
项目的目录结构
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

目录说明

mysite：项目名，项目的容器。

manage.py:项目启动入口，用于与django内部进行交互

init.py:初始化文件

settings.py:项目配置信息

urls.py:项目中webapi的路由配置

wsgi.py:一个 WSGI 兼容的 Web 服务器的入口

### 4、启动项目

```shell
python manage.py runserver
```

默认端口为127.0.0.1:8080,可以在runserver后添加自拟端口

### 5、创建应用

```shell
python manage.py startapp polls
```

### 6、创建视图

在polls/views.py中修改代码为：

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

在polls文件夹下创建urls.py并添加代码

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
在mysite/urls.py中修改代码为

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

运行 python  manage.py runserver 并访问 localhost:8000/polls(不是 localhost:8000)，将会看到Hello, world. You're at the polls index.



## 示例2： 