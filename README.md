# django_blog
creating a nice 2018 blog with backend as django2 and python3

# Start Django Project

1. Install virtualenv for creating virtual environment

	```
	pip install virtualenv
	```

2. Create a virtualenv and activate it

	```
	> virtualenv env
	> env/source/activate
	(env)>
	```

	**NOTE:** run all the upcoming commands inside virtualenv

3. Install requirements

	```
	pip install django
	```

4. Start Django Project

	```
	django-admin startproject website .
	```

	**NOTE:** trailing ```.``` at end tells django to create project files inside current directory, to check what I mean run the same command without ```.```

5. Run the server

	```
	python manage.py runserver
	```

**NOTE:** ignore any warnings and locate to [this](http://127.0.0.1:8000) url.

6. Create Super User

	```
	python manage.py createsuperuser
	```

Enter the **username** and **password** and email (optional) for django-admin site. This can be done while server is running, once done locate to [this]http://127.0.0.1:8000admin) url and enter your details.

**SOURCE**: [CodingForEntreprenuers](https://www.codingforentrepreneurs.com/projects/try-django-19/)

# Starting App
For starting new app in django run the following comman

```
python manage.py startapp posts
```

Notice a new folder **posts** created in root folder

**posts** app contains the following folder and files which django creates by itself

```
+ posts
	+ migrations
	- __init__.py
	- admin.py
	- apps.py
	- models.py
	- tests.py
	- views.py
```

The next thing we need to do is tell our django project about our posts app.
For that we need to add our app in project settings -- ```settings.py``` 

**website/setting.py**
```
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts', 		# posts app
]
```

Thats' it!

# Create Post Model
So according to Django [Docs](https://docs.djangoproject.com/en/2.1/topics/db/models/) Model is 

```
A model is the single, definitive source of information about your data. It contains 
the essential fields and behaviors of the data you’re storing. Generally, each model 
maps to a single database table.
```

So for creating a model for our posts app we will be writing code in **posts/models.py**

Django has built in Model and Model Fields so open **posts/models.py** file and you already have the ```models``` imported from ```django.db```

```
from django.db import models
```

Now we will create our own model particularly for our posts app which will have two
field actually four but the other two will be handled by django automatically

```
from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

```

You might be familiar with class inheritance in python ```class Post(models.Model):```
which is used here and we have made four fields 

1. **title** -- CharField with max characters 200 for title of post
2. **content** -- TextField for content of post
3. **timestamp** -- DateTimeField for recording time of creation of post 
	**Notice** the ```auto_now_add=True``` argument passed with ```DateTimeField```.
	This argument tells the django model to save the current date and time everytime a post object is created
4. **updated** -- DateTimeField with ```auto_now=True``` that tells django to save 
	current date and time everytime a already existing post is edited.
5. ```__str__``` method that returns ```title``` of post whenever the object is printed

# Model To Admin
Head onto Django Admin [Docs](https://docs.djangoproject.com/en/2.1/ref/contrib/admin/)
and check out how admin works in django

For actually registering our Post model into the admin site we need to do that using
```admin.site.register``` inside ```posts/admin.py```

```
from django.contrib import admin

from .models import Post

admin.site.register(Post)
```

So what we did is import our Post Model and then register it with admin.

Run the server again and head to [admin](http://127.0.0.1:8000/admin) site and you 
should see the ```Post``` Model, click on it and create few posts save them.

You will find that a list of posts appear with the heading as the title of the post
which is due to the ```__str__``` method inside ```model.py```

# Customizing Admin
In this section we will add some features to our admin site for Post model. For that we
need to create a [ModelAdmin](https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#modeladmin-objects)

Open **posts/admin.py** file again and create a new ModelAdmin class

```
from django.contrib import admin

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	class Meta:
		model = Post


admin.site.register(Post, PostModelAdmin)
```

This won't change anything on admin site, but using ModelAdmin [options](https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#modeladmin-options) would give us a whole lot of features.

We will add ```list_display``` feature that displays the fields inside the list/set into
the display of Model.

```
...
class PostModelAdmin(admin.ModelAdmin):
	list_display = ('title', 'timestamp')
	
	class Meta:
		model = Post
...
```

Notice how ```title``` field on Post Model page is clickable, we can make other fields
also clickable using ```list_display_links```

```
class PostModelAdmin(admin.ModelAdmin):
	list_display = ('title', 'timestamp', 'updated')
	list_display_links = ('title', 'timestamp')

	class Meta:
		model = Post
```

Again our model admin site is changed a bit.

There is also a ```list_filter``` feature that adds a filter onto right side with
the filter fields provided

```
	...
	list_filter = ('updated', 'timestamp')
	...
```

We can add a search field onto Model Site using ```search_fields``` feature like this

```
search_fields = ('title', 'content')
```

Enter the title or content of a post and search, you will get the results

One more very nice feature is quick editable using ```list_editable```

```
list_display_links = ('timestamp',)
list_editable = ('title',)
```

Since you added ```title``` to ```list_editable``` we need to remove the it from 
```list_display_links``` this makes sense cause we cannot make one field clickable as 
well as editable.

To change the model for example if we want to change the max_length paramter to 120 
then we would simply make changes in the file 
```title = models.CharField(max_length=120)``` but we need to do one more thing.

After making changes to fields in models we need to run ```makemigrations``` command
and then ```migrate```

```
python manage.py makemigrations
python manage.py migrate
```

If you have any questions regarding what we have done so far let me know at [CodeMentor](http://www.codementor.tk)

# [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)
1. Create
2. Retrieve
3. Update
4. Delete

Creating something refers to **CREATE**. Retrieving data is **RETRIEVE**. Updating the
existing data is **UPDATE** and lastly deleting the data comes under **DELETE**

In this section we will be creating **CRUD** functionality for our blog just like how
**Django Admin** works, our **CRUD** won't be as advanced and featureful as Django Admin
is but something that fulfills our requirements.

We are gonna create views for our CRUD functionality inside ```views.py```
We will be starting with [function based views](https://docs.djangoproject.com/en/2.1/topics/http/views/)

A simple function based view can be created through

**posts/view.py**
```
from django.shortcuts import render
from django.http import HttpResponse

def posts_home(request):
	return HttpResponse("<h1>Django Blog Home Page</h1>")

```

So we have a simple python function that returns a ```http.HttpResponse(html)```
object which will be shown on the url that is mapped with this view, more on that later.

Function based views are simple functions that needs to return some response everytime
the function is called. So our function takes in a argument ```request``` and it simply
returns and ```HttpResponse``` object with simple html inside it, this html will be 
rendered by browser so we don't need to worry about that.

Okay! We have our view ready now we want a url for this particular view.

**website/urls.py**
```
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', admin.site.urls),
]

```

Inside ```urls.py``` file we have just copy pasted the already existing url and changed
the string inside quotes to ```posts``` and if we run server 
```python manage.py runserver``` and navigate to [127.0.0.1:8000/posts/](http://127.0.0.1:8000/posts/) we find that we arrived at the same admin page. This is because we haven't mapped 
our url with the function based view ```posts_home(request)``` that we created.

To map our url with that view we need to import our view and define it with url

```
...
urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', posts_home, name='posts-home'),
]
```

Run server and navigate to refresh the page and you should see the html response that 
we returned from our **posts view**

This makes sense right! We created a view then a url for that view and joined them 
together and magic happens. We have our first MVC ready. The same way we will create the
other views for our **CRUD** and individual urls for each view.

You might be wondering that we didn't talked about the ```name``` argument. So let's talk 
about it. ```django.urls.path``` has ```name``` argument that is very useful in cases
when we want to denote our url so instead of completely writing our url 
```http://127.0.0.1:8000/posts/``` like this we can simply use the name ```posts-home```

We will dive into that later on.

So we have created our first url but we want to keep the **urls** for posts app in the app
itself so that our app is reusable and it comes under good practise.

Create a new file named ```urls.py``` inside posts app and paste the code from 
```website/urls.py```

**posts/urls.py**
```
from django.urls import path

from posts.views import posts_home

app_name = 'posts'

urlpatterns = [
    path('posts/', posts_home, name='posts-home'),
]

```

We just need to remove the admin url and its import because we don't need it here.

```
from django.urls import path

from posts.views import posts_home

app_name = 'posts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', posts_home, name='posts-home'),
]

```

We use [namespace](https://docs.djangoproject.com/en/2.1/topics/http/urls/#url-namespaces)
here. And when using namespace we need to define an ```app_name``` variable inside the 
app urls.

Run the server again and everything remains same.

All of this was for starting how to create a view and its url now we will actually create
views and urls for CRUD operations

Copy paste the posts_home view five times and make minor changes in them like changing the
function name and the html response to distinguish each page in browser

**posts/views.py**
```
from django.shortcuts import render
from django.http import HttpResponse

def post_create(request):
	return HttpResponse("<h1>Create view</h1>")


def post_detail(request):
	return HttpResponse("<h1>Detail view</h1>")


def post_update(request):
	return HttpResponse("<h1>Update view</h1>")


def post_list(request):
	return HttpResponse("<h1>List view</h1>")


def post_delete(request):
	return HttpResponse("<h1>Delete view</h1>")

```

Similarly import each view into urls and create url for each one

```
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
	path('detail/', post_detail, name='posts-detail'),
	path('update/', post_update, name='posts-update'),
	path('list/', post_list, name='posts-list'),
	path('delete/', post_delete, name='posts-delete'),
]
```

Run the server and if everything goes right we should have these urls ready

1. [CREATE VIEW](http://127.0.0.1:8000/posts/create/)
2. [UPDATE VIEW](http://127.0.0.1:8000/posts/update/)
3. [DELETE VIEW](http://127.0.0.1:8000/posts/delete/)
4. [LIST VIEW](http://127.0.0.1:8000/posts/list/)
5. [DETAIL VIEW](http://127.0.0.1:8000/posts/detail/)

Each of the url should display the returned ```HttpResponse```

Change urls, create more views, make same urls and change their orders and see what 
happens, the more you edit and write code yourself the more you will understand the 
django

# Django Templates

Open the project settings -- ```website/settings.py``` and go to

```
...

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

In ```'DIRS': []``` we need to add the path for our templates which will be in the root 
path so in the list we will add,

```
	...
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    ...
```

Here ```BASE_DIR``` refers to the root project location which basically is the path
where ```manage.py``` file lies and ```'templates'``` is the folder name

**Where Does BASE_DIR Come From ?**

If you look at the ```settings.py``` file again at the top

```
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
...
```

The Value is already assigned to ```BASE_DIR``` that generates the root location of 
django project automatically for us. If we change the project location then too our 
project would work because the location is not hardcoded here.

For more info on ```os``` module visit [docs](https://docs.python.org/3/library/os.html)

There is another way to render templates folder without specifying its settings, if you
are interested in that one be sure to contact me at [CodeMentor](http://codementor.tk)

Okay, Let's create the templates folder inside project root directory and inside 
**templates** create another file named ```index.html``` and put in some html in there.

```
├───posts
│   ├───migrations
│   │   └───__pycache__
│   └───__pycache__
├───templates
└───website
    └───__pycache__
    manage.py
    db.sqlite3
```

**index.html**
```
<!DOCTYPE html>
<html>
<head>
	<title>Django Blog</title>
</head>
<body>

	<h1>Django Templates On Duty</h1>

</body>
</html>
```

Now we need to tell django view to look for our template when rendering the webpage

**posts/views.py**
```
...
def post_list(request):
	return render(request, 'index.html', {})
...
```

Run the server again and locate to the [127.0.0.1:8000/posts/list](http://127.0.0.1:8000/posts/list) and you should see the html that exists in the template.

We used the **render** function that took **request**, **template** and a **dictionary**
. We will use the dictionary or more specifically context later on..

## Templates And Context
context is something that we can pass through our view function and display it in our
view template so basically what I mean is 

```
...
def post_list(request):
	context = {
		'title': 'django page'
	}
	return render(request, 'index.html', context)
```

We make a **dictionary** _(simple python dict)_ with a key and value pair and then we 
```return render``` with third argument as our context dict

To use the context variable we send in template we need to use ```{{ <context_key> }}```
in template

**index.html**
```
<!DOCTYPE html>
<html>
<head>
	<title>Django Blog</title>
</head>
<body>

	<h1>Django Templates On Duty</h1>
	{{ title }}

</body>
</html>
```

Refresh the page again and you should see the **value** of **title** from context 
displayed under H1 tag.

# Django Querysets
Before starting to display our the posts saved in our database onto the views we will be
handling the posts objects and querysets from the django shell itself

**django Shell**
```
python manage.py shell
```

This shell is a lot different from a python interpreter

```
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:
```

We can tinker with our database directly from the python shell 

```
In [1]: from posts.models import Post

In [2]: Post.objects.all()
Out[2]: <QuerySet [<Post: first post>, <Post: django post>]>

In [3]: Post.objects.get(title__icontains='django')
Out[3]: <Post: django post>

In [4]: Post.objects.create(title='New Post From Shell', content='POst')
Out[4]: <Post: New Post From Shell>

In [5]:
```

There are [lots](https://docs.djangoproject.com/en/2.1/ref/django-admin/#shell) of shell commands

Using the Django Docs you can practise the commands inside the django shell

## Queryset Views
In this section we will be displaying the data from backend onto the views.

**posts/views.py**
```
def post_list(request):
	queryset = Post.objects.all()
	context = {
		'title': 'django page',
		'queryset': queryset
	}
	return render(request, 'index.html', context)

```

And since we have passed our queryset in the context variable we just need

**templates/index.html**
```
<h3>{{ queryset }}</h3>
```

Run server and go to [http://127.0.0.1:8000/posts/list](http://127.0.0.1:8000/posts/list)
And you should see the queryset printed but what we want is more specific data so for that

**index.html**
```

	<h1>Django Templates On Duty</h1>
	{% for obj in queryset %}
		
		<ul>
			<li>
				<h3>{{ obj.title }}</h3>
				<li>{{ obj.content }}</li>
				<li>{{ obj.timestamp }}</li>
			</li>

		</ul>

	{% endfor %}

```

Above we run a **for** loop using **template tags** in django and using **dot notation**

## Post Detail View
We will be fetching the post details using the ```id``` attribute and for that we will
be using ```get_object_or_404```

**posts/views.py**
```
from django.shortcuts import render, get_object_or_404

...
def post_detail(request, id):
	object = get_object_or_404(Post, id=id)
	context = {
		'object': object
	}
	return render(request, 'posts/detail.html', context)
```

Notice the path for our template says ```detail.html``` file in **posts** folder

So create a folder named **posts** inside **templates** and create new file inside 
**posts** named ```detail.html```

**posts/detail.html**
```
<h1>Django Templates On Duty</h1>
		
		<ul>
			<li>
				<h3>{{ object.title }}</h3>
				<li>{{ object.content }}</li>
				<li>{{ object.timestamp }}</li>
				<li>{{ object.id }}</li>
			</li>

		</ul>
```

And since we changed our view to include a ```id``` argument we need to change our urls

**posts/urls.py**
```
urlpatterns = [
	path('create/', post_create, name='posts-home'),
	path('detail/<int:id>', post_detail, name='posts-detail'),
	path('update/', post_update, name='posts-update'),
	path('list/', post_list, name='posts-list'),
	path('delete/', post_delete, name='posts-delete'),
]

```

```'detail/<int:id>'``` url catches the number given in url in browser and our view function
catched that number as id and gets the object

**run the server** and visit to ...detail/1 url and you should see the details of the post
however if we visit to any non-existing id for example ...detail/10 we get a 
**Page Not Found** error and it makes sense right we don't wanna be showing posts details 
that doesn't exists so all of this is automatically done by ```get_object_or_404```
