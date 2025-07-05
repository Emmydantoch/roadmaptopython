#to build a new django application, you can use the following command:
# pip install django
# pip install virtualenvwrapper-win

# Create a new virtual environment for Django project and give it a name.
# mkvirtualenv myapp
# pip install django
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

