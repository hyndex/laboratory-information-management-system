![Made with Love in India](https://madewithlove.org.in/badge.svg) [![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

# laboratory-information-management-system

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

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
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver
	http://localhost:8000/users/Install

```
## Basic Login Details
```
	username:"admin",
	password:"qwerty"

```

## Login
```
	/users/Login/
	{
	"username":"admin",
	"password": "qwerty",
	}
```
## Logout
```
/users/Logout/
```
## Create User
```
Url:/users/User/
Json:
		{
		"username": "",
		"password": "",
		"email": "",
		"profile": {
			"id": null,
			"name": "",
			"phone": "",
			"address": "",
			"status": "",
			"image": null
		}
Response:
```
## Role User
```
Url:/users/Role/
Json:
		{
    	"role": ""
		}
Response:
```
## Assigning permission to Role
```
Url:/users/RolePermission/
Json:
		{
		"module": null,
		"role": null,
		"create": false,
		"read": false,
		"update": false,
		"delete": false,
		"type": null
		}
Response:
```
## Assigning Role to User
```
Url:/users/RolePermission/
Json:
		{
		"user": null,
		"role": null,
		"depertment": null
		}
Response:
[
    {
    "id": 1,
    "user": 1,
    "role": 1,
    "depertment": null,
    "date_updated": "2019-08-12T19:19:14.723297Z",
    "created_by": null,
    "updated_by": null
    }
]
```
## Creating a Depertment
```
Url:/lab/Section/
Json:
		{
		"name": "",
		"description": ""
		}
Response:
[
{
"id": 1,
"name": "Milk",
"description": "Milk and Milk Products",
"test_section": [],
"date_updated": "2019-08-12T19:45:29.316190Z",
"created_by": null,
"updated_by": null
}
]
```
## Creating a Test under a Depertment
```
Url:/lab/Test/
Json:
{
	"section_id": 1,
	"name": "carbs",
	"description": "carbohyddrate",
	"field_test": [{
			"name": "trans fat",
			"formula": "0",
			"measure": "mg",
			"uplimit": 100.0,
			"downlimit": 0.0
		},
		{
			"name": "good fat",
			"formula": "0",
			"measure": "mg",
			"uplimit": 100.0,
			"downlimit": 0.0
		}
	]
}
Response:
```
## Creating Client
```
Url:/lab/Client/
Json:
		{
		"name": "",
		"phone": "",
		"address": "",
		"status": "",
		"image": null
		}
Response:
[
{
"id": 1,
"name": "Anupam Saikia",
"phone": "987654",
"address": "sarupather",
"status": "",
"image": null,
"date_updated": "2019-08-13T00:32:43.302409Z",
"user": null,
"created_by": null,
"updated_by": null
}
]
```
## Registering a Sample under a client
```
Url:/lab/Sample/
Json:
		{
		"client_id": null,
		"name": ""
		}
Response:
```
