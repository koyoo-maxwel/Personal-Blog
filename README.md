# [Blog]()

## Description

website where you can create and share your opinions and other users can read and comment on them.
Users can subscribe to the blog to get the latest updates on articles.

The blog supports comments from readers and blog writers can determine whether to delete the comments or not. Users can also delete blog posts at their discretion.

After the writer has posted a new blog post, subscribers will receive an email notification with a link to the blog post.

### 14/09/2018

#### By[koyoo-maxwel](https://git.heroku.com/koyooblogit.git)

## Specifications

Get the specs [here](https://github.com/koyoo-maxwel/Personal-Blog/blob/master/SPEC.md)

## Set-up and Installation

### Prerequiites

    - Python 3.6
    - Ubuntu software

`Clone the Repo`

> Run the following command on the terminal:
`git clone https://github.com/koyoo-maxwel/Personal-Blog.git && cd Personal-Blog`

Install [Postgres](https://www.postgresql.org/download/)

### Create a Virtual Environment

Run the following commands in the same terminal:
'''bash

sudo apt-get install python3.6-venv
python3.6 -m venv virtual
source virtual/bin/activate
'''

### Install dependancies

Install dependancies that will create an environment for the app to run
`pip install -r requirements`

### Prepare environment variables

```bash
export DATABASE_URL='postgresql+psycopg2://<your-username>:<your-password>@localhost/blog'
export SECRET_KEY='Your secret key'
export DATABASE_URL_TEST='postgresql+psycopg2://<your-username>:<your-password>@localhost/blogtest'
export MAIL_SERVER='smtp.googlemail.com'
export MAIL_PORT=587
export MAIL_USE_TLS=1
export MAIL_USERNAME=<your-email>
export MAIL_PASSWORD=<your-password>
```

``

### Run Database Migrations

```bash
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
```

### Running the app in development

In the same terminal type:
`python3 manage.py server`

Open the browser on `http://localhost:5000/`

## Known bugs

Sending batch emails bug
If others are found, E-mail me at [koyoo maxwel](koyoomaxwel@gmail.com)

## Technologies used

    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

## Support and contact details

Contact me on developer[koyoo-maxwel](koyoomaxwel@mail.com) for any comments, reviews or advice.

### License

Copyright (c) [license](license)