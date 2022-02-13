# Buses Online Reservation

Mini web applications helping users to reserve buses online

## Project Description

Use virtual environment [venv](https://docs.python.org/3/library/venv.html) to encapsulate packages used

Use the web framework [Django](https://www.djangoproject.com/) to build project


## Installation

create virtual environment to isolate all packages used

```bash
python -m venv env
```

To activate virtual environment,

From ubuntu, use 

```bash
source env/bin/activate
```
 
From windows, use 

```bash
env\Scripts\activate
```

To install packages used in the program , 

```bash
pip install -r requirement.txt
```

To clone the repository

```bash
git clone https://github.com/Aya262/task3.git
```

navigate to manage.py location and run server
```bash
(env) aya@aya-Inspiron-5559:~/task3-master/tasks$ python manage.py runserver
```
In browser go to local host "http://127.0.0.1:8000/"



## Usage
access index page using

```python
http://127.0.0.1:8000/

# create account and login in to home page to choose bus routes and registraion period type
http://127.0.0.1:8000/home/

# for admin users can access inactivte registration 
http://127.0.0.1:8000/inactiveReservations/

# admin users also can activate registraions 
http://127.0.0.1:8000/activate/registration_id
