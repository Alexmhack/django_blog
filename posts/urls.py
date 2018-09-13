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
	path('create/', post_create, name='home'),
	path('<int:id>/', post_detail, name='detail'),
	path('<int:id>/update/', post_update, name='update'),
	path('list/', post_list, name='list'),
	path('<int:id>/delete/', post_delete, name='delete'),
]
