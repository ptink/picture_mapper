========================
Picture Mapper
========================

Picture mapper is an application for storing and viewing pictures from all over the world

Registered users can upload their pictures along with the location they were taken and add them to
a global interactive map featuring users photos from around the world

Project Layout
===================

This project uses the project layout from the Two Scoops of Django best practices guide. To create a project using this
template use the following startproject command:

``$ django-admin.py startproject --template=https://github.com/twoscoops/django-twoscoops-project/zipball/master --extension=py,rst,html <project_name>``

To Install Picture Mapper
===================

1. Clone the repo
2. Create a virtual environment (http://www.virtualenv.org).
3. Install dependencies:- ``$ pip install -r requirements.txt`` (Windows users: installing the PIL dependency on x64 can be a pain. You might find it easier to first activate the virtual environment and use:- ``$ easy_install PIL`` )
    1. The ``/requirements/`` folder contains requirements.txt files for different environments (local, production etc).
    2. By default, requirements.txt points to local.txt, the requirements for local environments
    3. To install requirements for a different environment either -
        1. Use pip install on that specific file e.g. ``$ pip install -r production.txt``
        2. Modify requirements.txt to point to the desired requirements file
4. Point the app to the correct settings file by either -
    1. Using the runserver settings command line argument e.g. ``$ django-admin.py runserver --settings=picture_mapper.settings.local``
    2. Creating a settings.py symlink to the correct settings file -
        1. Windows cmd - ``$ mklink .\settings.py .\local.py``
        2. Linux Terminal - ``$ ln -s local.py settings.py``
5. Run syncdb:- ``$ python manage.py syncdb``
6. Collect static files:- ``$ python manage.py collectstatic``

Project Dependencies
===================

django-south (http://south.readthedocs.org/en/latest/)
  Used for database migrations

PIL (http://www.pythonware.com/products/pil/)
  Required by django ImageField, also useful for
  extracting image meta-data

django-easy-maps (https://github.com/kmike/django-easy-maps)
  Useful app for embedding google maps into a page

geopy (https://github.com/geopy/geopy)
  Required by django-easy-maps, python geocoding toolbox

django-braces (http://django-braces.readthedocs.org/en/v1.2.2/)
  Useful when using class based views, patches several holes

django-registration (https://bitbucket.org/ubernostrum/django-registration/)
  Simple drop-in registration app

django-registration-bootstrap (https://pypi.python.org/pypi/django-registration-bootstrap)
  Bootstrap versions of the django-registration templates. The site presentation uses
  bootstrap for it's speed of creation/responsiveness so this saved some time

django-crispy-forms (https://github.com/maraujop/django-crispy-forms)
  required by django-registration-bootstrap. Also very useful for configuring forms

Notes
---------------

The ``SECRET_KEY`` in ``/settings/base.py`` is for local and testing use ONLY. In a production setting you
should override this (and any other sensitive settings information) using environment variables
