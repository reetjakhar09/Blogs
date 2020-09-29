from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings



urlpatterns=[
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('post_list/category_list/',views.category_list, name='category_list'),
	path('post/<int:pk>/',views.post_detail, name='post_detail'),
	path('post/new/',views.post_new, name='post_new'),
	path('edit_profile/<int:pk>/',views.edit_profile,name='edit_profile'),
	path('category_detail/<int:pk>/',views.category_detail,name='category_detail'),
	path('tag_detail/<str:slug>/',views.tag_detail,name='tag_detail'),
	path('like_post/<int:pk>/',views.like_post,name='like_post'),
	path('profile',views.profile,name='profile'),
	path('tag_list/',views.tag_list,name='tag_list'),
	path('register',views.register,name='register'),
	path('login',views.login,name='login'),
	path('logout',views.logout,name='logout'),
	
	path('', views.post_list, name='post_list'),

]