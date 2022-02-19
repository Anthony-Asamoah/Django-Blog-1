from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/<int:pk>/edit', views.edit_post, name='edit_post'),
	path('post/new', views.new_post, name='new_post'),
]
