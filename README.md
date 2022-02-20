
# Bookr-Store
 Bookr is ecommerce side project build with  python, django in backend
and tailwind-css and little js in front-end.
i have used postgreSQL for Database and deployed in AWS EC2 instance

## Features

- Registration
    - register for bookr account
    - login/logout/reset-password/change-password

- Account
    - auto-create user proile
    - edit user profile edit fname/lname/address
    - view order history for bookr purchase
    - download invoice for bookr purchase

- Blog
    - Create/Update/Delete  blog
    - add/delete comment on blogs
    - search for any blog

- Review
    - Create/Edit/Delete reviews on listed bookr
    - search for bookr

- cart
    - add to cart, update item quantity, delete items from cart, forward to check out
  
- order
    - create order, create order-items available in cart, 
    - create reacords for order, forwards to payments

- payments
    - razorpay intigration for handling payments,
    - transection-id, invoice genration,
    - sending invoice to registered email using asyn task with celery as workers and rabbitmq as message-broker

## Tech Stack

**Client:**  JS, TailwindCSS

**Server:** Django, python

**Database:** PostgreSQL

**Async Task:** Celery, Rabbitmq

**deployed on :** AWS EC2, gunicorn, NGINX, 




## Installation

Install BookR project in your local machine

```bash
git clone https://github.com/imchandr/Book-R.git

cd BookR

```

now install required packages and dependencies for project.
i have used pipenv in this project and if you have installed pipenv 
run

```bash
pipenv sync
```
now activate your virtual inviroment with command

```bash
pipenv shell
```

now before runing in your local env you need to make some tweek's 
- to run in development server, goto bookr-->settings.py set the 
```
DEBUG = False
```
- now if dont have postgreSQL installed, change the DATABSE in bookr-->settings.py to
```
DATABASES = {
    'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
- in bookr-->settings.py file comment email related settings and add to get emails in console
```
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

- now run makemigrations and migrate commands to create db
```
python manage.py makemigrations

python manage.py migrate
```
- to run the development server type and follow the commands
```
python manage.py runserver

```

- to populate the database i have created a custom command, run
```
python manage.py loadcsv --csv reviews/management/commands/WebDevWithDjangoData.csv
```


