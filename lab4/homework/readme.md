#  Dockerfying your Django application!


	> Start by creating your Django application.

- Run the following commands to set up your Django app 
```
- pipenv install django
- pipenv shell
- django-admin startproject bestProjectName
- python manage.py runserver
```
optional command :
```
- python manage.py startapp betterAppName
```
> be sure to add your app under the INSTALLED_APPS in your settings.py

- Add your html files under a **templates** folder
- Add your css and js files under a **static** folder
```
+-- bestProjectName
|  +-- betterAppName
|   |  +-- templates
|   |   | +-- how.html
|   |  +-- static
|   |   | +-- exhausting.css
|   |   | +-- isThis.js
```
- load your css and js files from your html file like so
```
<head>
{% load static%}
<link  rel='stylesheet'  href="{% static 'exhausting.css'%}">
</head>
<body>
<h1>Hello from the Docker side</h1>
</body>
<script  src="{% static 'isThis.js'%}"></script>
```

**Prepare Django app for Docker**

- Next we create the requirements.txt file that contains a list of all your python packages required to run your project.
> This file will be used in your Dockerfile
```
pip freeze > requirements.txt
```
- Create a Dockerfile and add the text below
```
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
```
- By now your folder hierachy should look something like this 
```
+-- bestProjectName
|  +-- betterAppName
|   |  +-- templates
|   |   | +-- how.html
|   |  +-- static
|   |   | +-- exhausting.css
|   |   | +-- isThis.js
+-- Dockerfile
+-- requirements.txt
```
**Docker Commands**

```
sudo docker build . -t python-django:v1

sudo docker run -d -p 8000:8000 -v "{FULL path to current folder}:/app" python-django:v1
```
> run **pwd** command to find full path to current folder

- Run this command to make sure your container is up and running
```
sudo docker container ls
```
-  visit http://localhost:8000/ to see your application up and running.