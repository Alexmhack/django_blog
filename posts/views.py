from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Post
from .forms import PostModelForm

def post_create(request):
	form = PostModelForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url)
	context = {
		'form': form
	}
	return render(request, 'posts/create.html', context)


def post_detail(request, id):
	object = get_object_or_404(Post, id=id)
	context = {
		'object': object
	}
	return render(request, 'posts/detail.html', context)


def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostModelForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		'instance': instance,
		'form': form
	}
	return render(request, "posts/update.html", context)


def post_list(request):
	queryset = Post.objects.all()
	context = {
		'title': 'django page',
		'queryset': queryset
	}
	return render(request, 'posts/list.html', context)


def post_delete(request):
	return HttpResponse("<h1>Delete view</h1>")
