from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post

def post_create(request):
	return HttpResponse("<h1>Create view</h1>")


def post_detail(request, id):
	object = get_object_or_404(Post, id=id)
	context = {
		'object': object
	}
	return render(request, 'posts/detail.html', context)


def post_update(request):
	return HttpResponse("<h1>Update view</h1>")


def post_list(request):
	queryset = Post.objects.all()
	context = {
		'title': 'django page',
		'queryset': queryset
	}
	return render(request, 'posts/list.html', context)


def post_delete(request):
	return HttpResponse("<h1>Delete view</h1>")
