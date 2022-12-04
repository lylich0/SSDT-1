# SSDT | lab 1
by Mila Bibik, group IO-01

# Description
This project was made for educational purposes.

As the usage of databases is prohibited in this lab, I came up with the following solution:

1. send all post requests to create the list of users, categories and records.
2. now you can play with get requests :)

All data will be erased.

Basic endpoints:
* Create user
* Create expanse category
* Create expanse record
* Get list of categories
* Get list of records for a sprecific user
* Get list of records in specific category for a sprecific user

Domain:
```
https://backend-lab1-mbibik.herokuapp.com/swagger/
```

# Instructions
To run this project locally try:
```
git clone https://github.com/lylich0/SSDT-1.git
```
```
docker build -t lab1-app:latest .
```
```
docker-compose build
docker-compose up
```
