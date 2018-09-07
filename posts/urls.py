from django.urls import path

from posts.views import posts_home

app_name = 'posts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', posts_home, name='posts-home'),
]
