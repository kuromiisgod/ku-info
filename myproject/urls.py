"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from kublog import views


admin.site.site_header = 'kublog管理者用サイト'
admin.site.index_title = 'ホーム'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name='home'),
    path('append_post/', views.append_post, name='append_post'),
    path('post_one/<int:post_id>/', views.post_one, name='post_one'),
    path('post_one/post_delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('post_one/post_edit/<int:post_id>/', views.post_edit, name='post_edit'),
    path('contact_form/', views.contact_form, name='contact_form'),
    path('search_classroom/', views.search_classroom, name='search_classroom'),
    path('accounts/', include('allauth.urls')),
    
]