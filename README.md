# drf-serializer-class-dynamic
Decide serializer class dynamically based on viewset actions

## Installation steps

> I assume python3.7 is available in system path at `/usr/bin` or `/usr/local/bin` directory. If you don't have it then I would recommend to install it (for example, `sudo apt install python3.7`)!
>
> Also, please upgrade pip via `pip install --upgrade pip --user`

- clone the repository via `git clone https://github.com/rsudip90/drf-serializer-class-dynamic.git` and change directory to it via `cd drf-serializer-class-dynamic`
- create virtualenv via `virtualenv --python=/usr/bin/python3.7 venv`
- active virtualenv via `source venv/bin/activate`\
- install the dependencies via `pip install -r requirements.txt`
- change directory to `webapp` via `cd webapp`
- run migrations via `python manage.py migrate`
- load fixtures available for `sample` app via `python manage.py loaddata sample`
- run the web application server via `python manage.py runserver`
- There are three users available in fixtures as follows:

    | email               | password | is_superuser | is_staff |
    |---------------------|----------|--------------|----------|
    | admin@localhost.com | admin    | yes          | yes      |
    | frank@raindrops.com | 1234     | no           | no       |
    | joe@raindrops.com   | 1234     | no           | no       |

- get logged in via username `frank@raindrops.com` at url `http://localhost:8000/api-auth/login/`
- visit `http://localhost:8000/api/v1/` and that's it.