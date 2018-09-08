from django.shortcuts import render
from django.http import HttpResponse

def post_create(request):
	return HttpResponse("<h1>Create view</h1>")


def post_detail(request):
	return HttpResponse("<h1>Detail view</h1>")


def post_update(request):
	return HttpResponse("<h1>Update view</h1>")


def post_list(request):
	return render(request, 'index.html', {})


def post_delete(request):
	return HttpResponse("<h1>Delete view</h1>")
