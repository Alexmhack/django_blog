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
	path('detail/', post_detail, name='posts-home'),
	path('update/', post_update, name='posts-home'),
	path('list/', post_list, name='posts-home'),
	path('delete/', post_delete, name='posts-home'),
]
