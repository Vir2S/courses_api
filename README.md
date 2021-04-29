# Courses REST API with Django Rest Framework

**Installation:**

_Linux:_ run the script install_linux.sh

_Windows:_ run the script install_windows.cmd

After the script finishes, you need to make database migrations.
To do this, run the command on the command line:

`python manage.py migrate`

Then you have to create superuser:

`python manage.py createsuperuser`

and follow instructions on the screen.

**Start:**

Run command under command line:

`python manage.py runserver`

Put link in your browser

`localhost:8000/api/v1/`

**Endpoints:**

`/api/v1/` - courses list (GET)

`/api/v1/add/` - create a new course (POST)

`/api/v1/some_id/` - get full course description (GET, PUT, DELETE)