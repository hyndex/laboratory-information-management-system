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
## Creating a Depertment
```
Url:/lab/Section/
Json:
		{
			"name": "",
			"description": ""
		}
Response:
```
## Creating a Test under a Depertment
```
Url:/lab/Test/
Json:
		{
			"section_id": null,
			"name": "",
			"description": "",
			"field_test": [
									{
									"name":"",
									"formula":"",
									"measure':"",
									"uplimit":"",
									"downlimit""":
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