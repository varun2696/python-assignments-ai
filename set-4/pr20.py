# 20. **Basic Django Web App**: Create a basic web application using Django that has two routes, one that displays "Hello, World!" and one that displays "Goodbye, World!".
#     - *Input*: Visit "/", Visit "/goodbye"
#     - *Output*: "Hello, World!", "Goodbye, World!"



# To create a basic web application using Django with two routes, you need to follow these steps:

# Install Django:
# First, make sure you have Django installed. If you haven't installed it yet, you can do so using pip:


# pip install Django

# Create a Django project:
# Open your terminal or command prompt, navigate to the directory where you want to create the project, and run the following command:

# django-admin startproject myproject
# Replace myproject with the name you want to give your project.

# Create a Django app:
# Change into the project directory and create a Django app using the following command:

# bash

# cd myproject
# python manage.py startapp myapp
# Replace myapp with the name you want to give your app.

# Define the views:
# Open the views.py file inside the myapp directory and define the views for both routes:

# python

# from django.http import HttpResponse

# def hello_view(request):
#     return HttpResponse("Hello, World!")

# def goodbye_view(request):
#     return HttpResponse("Goodbye, World!")

# Define the URLs:
# Create a urls.py file inside the myapp directory and define the URLs for the views:


# from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.hello_view, name='hello'),
#     path('goodbye/', views.goodbye_view, name='goodbye'),
# ]

# Connect the app to the project:
# Open the urls.py file inside the myproject directory and include the URLs of the myapp:


# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('myapp.urls')),
# ]

# Run the development server:
# In the terminal, run the following command to start the development server:


# python manage.py runserver
