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
