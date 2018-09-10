from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def post_create(request):
	return HttpResponse("<h1>Create view</h1>")


def post_detail(request):
	return HttpResponse("<h1>Detail view</h1>")


def post_update(request):
	return HttpResponse("<h1>Update view</h1>")


def post_list(request):
	queryset = Post.objects.all()
	context = {
		'title': 'django page',
		'queryset': queryset
	}
	return render(request, 'index.html', context)


def post_delete(request):
	return HttpResponse("<h1>Delete view</h1>")
