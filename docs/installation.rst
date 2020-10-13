Installation
============

Database
########

You will need a working database for this project. We recommend the use of PostgreSQL but any database working with django (see `here <https://docs.djangoproject.com/en/3.0/ref/databases/>`_) will do the trick.

However, please note that this software should be linked to mail server softwares like postfix and dovecot and that any datbase might not work with those. Please see the documentations of those before choosing any database.

You will need to create, before installatiom, a database (e.g. ``dinomail``) and a user (e.g. ``dinomail``) with some password that we will denote ``secret`` for the rest of this page.

Clone and install dependencies
##############################

First you will have to clone the Github repository of the project. We recommmend you to clone from the last release.

.. code-block:: bash

    git clone https://github.com/nanoy42/dinomail


Then you need to install the dependencies. There is a Pipfile, from which you can just do 

.. code-block:: bash

    pipenv install

Or you can use the requirements.txt file :

.. code-block:: bash

    pip3 install -r requirements.txt

Apply migrations and create superuser
#####################################

You cna populate the database with the schema with the command 

.. code-block:: bash

    python3 manage.py migrate

You can then create a superuser by running the command 

.. code-block:: bash

    python3 manage.py createsuperuser

Development installation
########################

You can install the dev requirements with 

.. code-block:: bash
    
    pipenv install --dev

or 

.. code-block:: bash

    pip3 install -r dev-requirements.txt

.. warning::
    You may have to manually create directories ``src/media/original`` and ``src/media/watermark`` in order to successfully run the tests.
