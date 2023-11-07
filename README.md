# Django-Mini-Projects

This is a Django Tutorial. This repo is divided into several Lectures, where each lecture would contain notes which includes the summary of what is there in the lecture. With each lecture, Django is explored with the help of projects to help understand how we can use Django to create a full fleged website. Each project has some new concepts which would contibute to learning Django in depth. 

### Steps to create a Django project

1. open cmd where we want the Django project, open cmd in that location.
2. python -m venv venv (the name of our virtual environment is venv here)
3. then type, venv\Scripts\activate
4. our virtual environment is activated
5. now install django by pip install django
6. Django is installed in your virtual environment venv
7. Now create your project by the following command:
	django-admin startproject projectname

8. our project is created with a folder projectname
9. inside that folder we again have a sub folder named projectname that folder has two important files namely --> settings.py and urls.py
10. now, we create an app where we build our actual project. To create an app we write the following command:
	python manage.py startapp appname
11. the appname folder contains important files such as models.py, views.py, etc
12. now we can edit the different files and create our project.
13. To run the project --> python manage.py runserver

