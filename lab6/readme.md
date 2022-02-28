#  Docker-compose-fying your Django application!


- Start by creating your Django application with postgres as your default Database.
- Create a database for your project using postgres
```
sudo -u postgres createdb lab6
```
- make the necessary migrations and migrate
```
python manage.py makemigrations betterAppName
python manage.py migrate
```
- Create a Dockerfile inside the main app folder 
```
FROM python:3.9.7-buster

WORKDIR /home/app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./app .

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
```
- Create docker-compose.yml file outside the app directory
```
version: "3"
services:

		api:
			build:
					context: ./app
					dockerfile: Dockerfile
			ports:
					- "8000:8000"
			volumes:
					- ./app:/home/app
		postgres:
		image: postgres:14.1
		healthcheck:
				test: [ "CMD", "pg_isready", "-q", "-d", "postgres", "-U", "root" ]
				timeout: 45s
				interval: 10s
				retries: 10
		restart: always
		environment:
				- POSTGRES_USER=postgres
				- POSTGRES_PASSWORD=123456
				- APP_DB_USER=docker
				- APP_DB_PASS=docker
				- APP_DB_NAME=docker
		volumes:
				- postgres-volume:/var/lib/postgresql/data
		ports:
				- 5432:5432
volumes:
	postgres-volume:
```
> Your app directory should look like this

```
+-- bestProjectName
|  +-- betterAppName
|  +-- Dockerfile
+-- docker-compose.yml
```
- Next we build the docker-compose file
```
sudo docker-compose up --build -d
```
> This will take some time the first time

- Check the docker container ids for your app and postgres to interact with them using the following commands
- Create the database inside the posgress container 
```
sudo docker ps
sudo docker exec -it lab6_postgres_1 bash
psql -U postgres
CREATE DATABASE lab6;
```
- similarly, once the database is created we perform the migrations on the app container
```
sudo docker exec -it lab6_api_1 bash
python manage.py makemigrations betterAppName
python manage.py migrate
```
- Upon exiting the containers now you can go to http://localhost:8000/ and your app will be up and running on port 8000 and your postgres database on port 5432