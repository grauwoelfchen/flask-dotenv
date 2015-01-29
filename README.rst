Flask-DotEnv
------------

Adds support for .env file to flask applications.


Install
-------

::

    $ pip install Flask-DotEnv


Usage
-----

Basic usage.

::

    from flask import Flask
    from flask.ext.dotenv import DotEnv
    
    app = Flask(__name__)
    env = DotEnv(app)

As factory pattern.

::

    env = DotEnv()
    env.init_app(app)

You can pass .env file path as second argument.

::

    env.init_app(app, "/path/to/.env")

``os.path.join(os.getcwd(), '.env')`` is default.


Or ... just use simply ``pytho-dotenv`` without this pacage :-p

::

    # from README.md of python-dotenv
    import dotenv
    dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))


Development
-----------

Run unittest.


::

    $ python tests.py


Link
----

Inspired from:

* `python-dotenv`_
* `django-dotenv`_

See also another packages, its use config:

* `Flask-EnvConfig`_
* `Flask-UserEnvConfig`_


License
-------

BSD 2-Clause License


.. _python-dotenv: https://github.com/theskumar/python-dotenv
.. _django-dotenv: https://github.com/jpadilla/django-dotenv
.. _Flask-EnvConfig: https://bitbucket.org/romabysen/flask-envconfig
.. _Flask-UserEnvConfig: https://github.com/caustin/flask-userenvconfig
