from django.urls import path

from posts.views import (
	post_create,
	post_detail,
	post_update,
	post_list,
	post_delete,
)

app_name = 'posts'

urlpatterns = [
	path('create/', post_create, name='posts-home'),
	path('detail/<int:id>', post_detail, name='posts-detail'),
	path('update/', post_update, name='posts-update'),
	path('list/', post_list, name='posts-list'),
	path('delete/', post_delete, name='posts-delete'),
]
