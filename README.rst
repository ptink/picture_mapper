========================
Picture Mapper
========================

Picture mapper is an application for storing and viewing pictures from all over the world.

Registered users can upload their pictures along with the location they were taken and add them to
a global interactive map featuring users photos from around the world.

Project Layout
===================

This project uses the project layout from the Two Scoops of Django best practices guide. To create a project using this
template use the following startproject command:

$ django-admin.py startproject --template=https://github.com/twoscoops/django-twoscoops-project/zipball/master --extension=py,rst,html <project_name>

To Install Picture Mapper
===================

1. Clone the repo
2. Create a virtual environment (http://www.virtualenv.org).
3. Install dependencies:- $ pip install -r requirements.txt
    i. The /requirements/ folder contains requirements.txt files for different environments (local, production etc).
    ii. By default, requirements.txt points to local.txt, the requirements for local environments.
    iii. To install requirements for a different environment -
        a. Use pip install on that specific file e.g. $ pip install -r production.txt
        b. Modify requirements.txt to point to the desired requirements file.
4. Point the app to the correct settings file by -
    i. Using the runserver settings command line argument e.g. $ django-admin.py runserver --settings=picture_mapper.settings.local
    ii. Creating a settings.py symlink to the correct settings file -
        a. Windows cmd - mklink .\settings.py .\local.py
        b. Linux Terminal - ln -s local.py settings.py
5. Run syncdb:- $ python manage.py syncdb
6. Collect static files:- $ python manage.py collectstatic


Notes
---------------

The SECRET_KEY in /settings/base.py is for local and testing use ONLY. In a production setting you
should override this (and any other sensitive settings information) using environment variables.
