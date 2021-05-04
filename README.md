# Quick overview
This is a simple API for courses. Created as test task for Yalantis Python School.

Developed using:
Python v3.8.2, Django framework, Django Rest framework and Django filter.

## Installation Guide
1. Setup virtual enviroment
```bash
mkdir MyProject && cd MyProject
python3 -m venv venv
source venv/bin/activate
```
2. Clone project
```bash
git clone https://github.com/Cyber-Shai-Hulud/Courses_catalog.git
```

3. Install packages
```bash
pip install -r requirements.txt
```

4. Create database
```bash
python manage.py makemigrations
python manage.py migrate
```

## Usage
1. Run server
```bash
python manage.py runserver
```
2. Access endpoint for list view, post requests, search and filter
```bash
http://127.0.0.1:8000/
```

3. Access endpoint for detail view, deletion and change attributes
```bash
http://127.0.0.1:8000/{id}/
```

## Test
Tests available via Postman

[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.postman.co/run-collection/dd13c8e145d2622536ae?action=collection%2Fimport)
