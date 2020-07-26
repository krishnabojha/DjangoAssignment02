from django.contrib import admin
from django.urls import path
from Blog.views import homePage, blogPage, profilePage, writeBlog, readBlog, editBlog

urlpatterns = [
    path('',homePage),
    path('home/', homePage),
    path('list/', blogPage),
    path('profile/', profilePage),
    path('myblog/', writeBlog),
    path('read/<pk>',readBlog),
    path('edit/<pk>',editBlog),
]