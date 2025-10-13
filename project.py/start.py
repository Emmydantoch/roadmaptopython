#to build a new django application, you can use the following command:
# pip install django
# pip install virtualenvwrapper-win

# Create a new virtual environment for Django project and give it a name.
# mkvirtualenv myapp
# pip install django
# python -m django startproject weather_detector
# django-admin startproject myproject
# cd myproject
# to be sure you are right directory, use dir.
# python manage.py startapp myapp
# # This will create a new Django application named "myapp" within the "myproject" directory.

# create a file called url.py in 'myapp'
# configure the urls.py file to include the app's URLs.
#configure views.py file in 'myapp' to define views for the application.

# run app with manage.py runserver
# This will start the Django development server, and you can access your application at http://127.0.0.1:8000/
# go to the main project named myproject and open the urls.py file. and import include e.g
# from django.urls import include, path

# then from our views.py file we return HttpResponse and, import e.g
# from django.http import HttpResponse
# def index(request):
    # return HttpResponse("Hello, world! This is my Django app.")
    
# since we can not create all html codes in index function, we can create a template folder in the app directory and create an html file in it.
# then we can use render function to render the html file.

# also make sure to edit the settings.py as DIR_BASE to include the templates directory,    

# now we have Activate the virtual environment.
# deactivate # to deactivate the virtual environment
# workon myapp: this is used to activate the virtual environment that we want to work on

# used to migrate to AdminData base
# python manage.py 
# to connect postgressql database to django
# pip install psycopg2
# then in settings.py file, change the database settings to connect to postgresql database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'your_db_name',
#         'USER': 'your_db_user',
#         'PASSWORD': 'your_db_password',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
# then run the migrations
# python manage.py migrate
# python manage.py runserver
# to create a superuser for admin panel
# python manage.py createsuperuser
# then follow the prompts to create a superuser account.
# then you can access the admin panel at http://127.0.0.1:8000/admin/
# to create models in models.py file in 'myapp'
# then run the migrations to create the tables in the database
# python manage.py makemigrations myapp
# python manage.py migrate  
# then you can register the models in admin.py file in 'myapp' to make them accessible in the admin panel.
# from .models import MyModel
# admin.site.register(MyModel)
# then you can create views in views.py file in 'myapp' to handle requests and return responses.
# then you can create templates in templates directory in 'myapp' to render HTML pages.
# then you can create static files in static directory in 'myapp' to include CSS, JavaScript, and images.
# then you can create forms in forms.py file in 'myapp' to handle user input
# then you can create tests in tests.py file in 'myapp' to test the application.
# then you can deploy the application to a web server or cloud platform to make it accessible to users.
# to destroy all data in sqlite3 use
# python manage.py flush
# this is used to create a token for aunthentication
# manage.py_drf_create_token admin