from re import template
# from django.contrib.auth import views as auth_views
from django.urls import path
from .views import UserRegisterView ,UserUpdateView,PasswordChangeView ,password_success ,ShowProfilePageView, EditProfilePageView ,CreateProfilePageView

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name = 'register'),
    path('edit_profile/',UserUpdateView.as_view(),name = 'edit_profile'),
    path('password/',PasswordChangeView.as_view(),name = 'password_change'),
    path('password_success/',password_success,name = 'password_success'),
    path('<int:pk>/Profile',ShowProfilePageView.as_view(),name = 'profile_page'),
    path('<int:pk>/edit_profile_page',EditProfilePageView.as_view(),name = 'edit_profile_page'),
    path('create_profile_page/',CreateProfilePageView.as_view(),name = 'create_profile_page'),

]
