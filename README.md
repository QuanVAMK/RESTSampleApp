# RESTSampleApp

# WRITTEN BY QUAN MINH HONG NGUYEN

## This project is written and has been tested successfully on Windows OS.

#### This project is a simple demonstration of the use of Django REST framework for building Web APIs. It is done with the purpose of learning REST, what is REST, what functionality does it have and how do we implement it in our website. Aside from the template used in the [quickstart tutorial](http://www.django-rest-framework.org/tutorial/quickstart/), 1 new model was created called Stocks.

a. Installation 

1. Download the project by cloning from github or downloading the ZIP file. Extract it, then open CMD and change directory to where the project is located. For example:
```
E:\RESTSampleApp-master
```
2. In the working directory, set the environment path to where your python application was installed:
``` 
set PATH=%PATH%;yourdrive:\python;yourdrive\python\Scripts
```
3. Create a new virtual environment to isolate our package dependencies locally (note that python3.6 was installed so ```virtualenv``` command was also included in the downloading package). 
Then activate the environment: 
```
path\to\env\Scripts\activate
```
4. Install django and the REST framework in our local virtual environment
```
pip install django
pip install djangorestframework
```
5. go into our project directory (in the example, it is located in ```E:\RESTSampleApp-master\RESTSampleApp-master```)

6. In the project, the database has already been synced, so we don't have to run the command ``` python manage.py migrate ```
7. Run the server: ``` python manage.py runserver ``` and go to the described local server.
8. The Stocks model should have been registered, we can go in and add more stock tables or retrieve the tables.

b. Updating models
To add and play with the models, these files should be edited: models.py, serializers.py, admin.py, views.py, urls.py and settings.py . You could then update the database by make migrations: 
```
python manage.py makemigrations yourapp
```
If you want to make further changes, visit [Django REST framework site](http://www.django-rest-framework.org/tutorial/quickstart/#project-setup) for more tutorials and in-depth understandings.

c. Credits and acknowledgements: this project is made from the tutorials provided by [Django REST framework website](http://www.django-rest-framework.org).