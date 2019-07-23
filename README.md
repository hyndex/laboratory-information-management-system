# SIMPLE LIMS API WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python 3.6
- Django (2.1)
- Django REST Framework
- Django Rest Auth

## Installation
```
	pip install django
	pip install djangorestframework
	pip install django-rest-auth
	pip install django-allauth
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource, `Sample`, so we will use the following URLS - `/Sample/` and `/Sample/<id>` for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`Sample` | GET | READ | Get all Sample
`Sample/:id` | GET | READ | Get a single Sample
`Sample`| POST | CREATE | Create a new Sample
`Sample/:id` | PUT | UPDATE | Update a Sample
`Sample/:id` | DELETE | DELETE | Delete a Sample



First, we have to start up Django's development server.
```
	python manage.py runserver
```
Only authenticated users can use the API services, for that reason if we try this:
```
	http  http://127.0.0.1:8000/api/v1/Sample/3
```
we get:
```
 {  "detail":  "You must be authenticated"  }
```
Instead, if we try to access with credentials:
```
	http http://127.0.0.1:8000/api/v1/Sample/3 "Authorization: Token 7530ec9186a31a5b3dd8d03d84e34f80941391e3"
```