
from turtle import home
from unicodedata import name
from django.urls import path
from .views import HomeView ,ArticleDetailView ,AddPostView,UpdatePostView,DeletePostView, CategoryView ,CategoryViewList,LikeView,AddCategoryView, AddComment

urlpatterns = [
    path('',HomeView.as_view(), name= 'home'),
    path('artical/<int:pk>',ArticleDetailView.as_view(), name= 'article_detail') ,
    path('add_post/',AddPostView.as_view(), name= 'add_post') ,
    path('artical/edit/<int:pk>',UpdatePostView.as_view(), name= 'update_post') ,
    path('artical/<int:pk>/remove',DeletePostView.as_view(), name= 'delete_post') ,
    path('category/<str:cats>/', CategoryView, name= 'category') ,
    path('category-list/', CategoryViewList, name= 'category-list') ,
    path('like/<int:pk>', LikeView, name='like_post') ,
    path('add_category/', AddCategoryView.as_view(), name='add_category') ,
    path('artical/<int:pk>/add_comment',AddComment, name= 'add_comment'),


]