# RESTSampleApp

# WRITTEN BY QUAN MINH HONG NGUYEN

## This project is written and has been tested successfully on Windows OS.
## The project is only compatible with python 3.x, if you use python 2.x, you need to delete the ``` from exec  ``` line in manage.py file.

#### This project is a simple demonstration of the use of Django REST framework for building Web APIs. It is done with the purpose of learning REST, what is REST, what functionality does it have and how do we implement it in our website. Aside from the model snippets used in the [tutorial](http://www.django-rest-framework.org/tutorial/1-serialization/), 2 new model were created called Bond and Company.

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
4. Install django and the REST framework in our local virtual environment:
```
pip3 install django
pip3 install djangorestframework
pip3 install pygments (to use snippets or you could delete it)
```
5. go into our project directory (in the example, it is located in ```E:\RESTSampleApp-master\RESTSampleApp-master```)

6. In the project, the database has already been synced, so we don't have to run the command ``` python manage.py migrate ```
7. Run the server: ``` python manage.py runserver ``` and go to the described local server (we have 2 default usernames for testing:
admin:password123 & admin2:password1234
8. The models should have been registered, we can go in and do basic HTTP methods to retrieve, update, create or delete the records
in the tables.

b. Updating models
To add and play with the models, these files should be edited: models.py, serializers.py, views.py, urls.py and settings.py . You could then update the database by make migrations: 
```
python manage.py makemigrations yourapp
```
If you want to make further changes, visit [Django REST framework site](http://www.django-rest-framework.org/tutorial/1-serialization/) for more tutorials and in-depth understandings.

c. Credits and acknowledgements: this project is made from the tutorials provided by [Django REST framework website](http://www.django-rest-framework.org).
