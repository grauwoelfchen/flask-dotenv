Flask-DotEnv
------------

| Adds support for .env file to flask applications.
| From version ``0.0.3``, set config var without ``os.environ``.


`Flask-DotEnv` will directly set (add, update and map as alias) variable frob `.env` file.


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

| This env module may be usefull in your Config class.
| e.g.

::

    class Config:
        SECRET_KEY = ":'("
        ...

        @classmethod
        def init_app(self, app)
            env = DotEnv()
            env.init_app(app)

            # alias is optional
            # this will set var like a `DEVELOPMENT_DATABASE_URL` as `SQLALCHEMY_DATABASE_URI`
            prefix = self.__name__.replace('Config', '').upper()
            env.alias(maps={
                prefix + '_DATABASE_URL': 'SQLALCHEMY_DATABASE_URI'
            })


You can pass .env file path as second argument of ``init_app()``.

::

    env.init_app(app, env_file="/path/to/.env", verbose_mode=True)

| The second argument (``env_file``) is optional. default is ``os.path.join(os.getcwd(), '.env')``.
| The third argument (``verbose_mode``) is also optional. default ``False``.


| If ``verbose_mode`` is True, then server outputs which vars will be set.
| like this:

::

    * Overwriting an existing config var: SECRET_KEY
    * Setting an entirely new config var: DEVELOPMENT_DATABASE_URL
    * Mapping a specified var as a alias: DEVELOPMENT_DATABASE_URL => SQLALCHEMY_DATABASE_URI
    ...


`alias()` method takes a dict argment.

::

    env.alias(maps={
      'TEST_DATABASE_URL': 'SQLALCHEMY_DATABASE_URI',
      'TEST_HOST': 'HOST'
    })



Development
-----------

Run unittest.

::

    $ python tests/tests.py



Link
----

Inspired from:

* `python-dotenv`_
* `django-dotenv`_

See another packages, its also set config vars:

* `Flask-EnvConfig`_
* `Flask-UserEnvConfig`_


License
-------

BSD 2-Clause License


.. _python-dotenv: https://github.com/theskumar/python-dotenv
.. _django-dotenv: https://github.com/jpadilla/django-dotenv
.. _Flask-EnvConfig: https://bitbucket.org/romabysen/flask-envconfig
.. _Flask-UserEnvConfig: https://github.com/caustin/flask-userenvconfig
