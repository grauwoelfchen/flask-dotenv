Flask-DotEnv
------------

.. image:: https://travis-ci.org/grauwoelfchen/flask-dotenv.svg?branch=master
    :target: https://travis-ci.org/grauwoelfchen/flask-dotenv

.. image:: https://img.shields.io/pypi/v/Flask-Dotenv.svg
    :target: https://pypi.python.org/pypi/Flask-Dotenv/

| Adds support for .env file to flask applications.
| From version ``0.0.3``, set config var without ``os.environ``.
|


`Flask-DotEnv` will directly set (add, update, map as alias and eval as literal) variable from ``.env`` file,
and cast to Python native types as appropriate.

(optional)

* ``alias()`` makes alias var
* ``eval()`` evaluate var to literal (via ast)


Install
-------

::

    $ pip install Flask-DotEnv



Usage
-----

**********
DotEnv
**********

::

    from flask import Flask
    from flask.ext.dotenv import DotEnv

    app = Flask(__name__)
    env = DotEnv(app)

As factory pattern.

::

    env = DotEnv()
    env.init_app(app)

| This ``env`` module may be usefull in your Config class.
| e.g.

::

    class Config:
        SECRET_KEY = ":'("
        ...

        @classmethod
        def init_app(self, app)
            env = DotEnv()
            env.init_app(app)

Then in your app:

::

    from config import config

    app = Flask(__name__)
    app.config.from_object(config[config_name])

See also:

`flask.Config.from_object <http://flask.pocoo.org/docs/0.10/api/#flask.Config.from_object>`_ (API — Flask Documentation)

**********
Arguments
**********

You can pass ``.env`` file path as second argument of ``init_app()``.

::

    env.init_app(app, env_file="/path/to/.env", verbose_mode=True)

| The second argument (``env_file``) is optional. default is ``os.path.join(os.getcwd(), '.env')``.
| The third argument (``verbose_mode``) is also optional. default ``False``.

| If ``verbose_mode`` is True, then server outputs nice log message which vars will be set.
| like this:

::

    * Overwriting an existing config var: SECRET_KEY
    * Setting an entirely new config var: DEVELOPMENT_DATABASE_URL
    * Casting a specified var as literal: MAIL_PORT => <class 'int'>
    * Mapping a specified var as a alias: DEVELOPMENT_DATABASE_URL -> SQLALCHEMY_DATABASE_URI
    ...

**********
Alias
**********

``alias()`` method takes a dict argment.

::

    env.alias(maps={
      'TEST_DATABASE_URL': 'SQLALCHEMY_DATABASE_URI',
      'TEST_HOST': 'HOST'
    })

This is example usage of ``alias``:

::

    class Config:
        SECRET_KEY = ":'("
        ...

        @classmethod
        def init_app(self, app)
            env = DotEnv()
            env.init_app(app)

            # this will set var like a `DEVELOPMENT_DATABASE_URL` as `SQLALCHEMY_DATABASE_URI`
            prefix = self.__name__.replace('Config', '').upper()
            env.alias(maps={
                prefix + '_DATABASE_URL': 'SQLALCHEMY_DATABASE_URI'
            })


    class DevelopmentConfig(Config):
        DEBUG = True
        SQLALCHEMY_DATABASE_URI = None


    config = {
        'development': DevelopmentConfig
    }


**********
Eval
**********

``eval()`` method takes a dict argment.

::

    env.eval(keys={
      'MAIL_PORT': int,
      'SETTINGS': dict
    })

This is example usage of ``eval``:

::

    class Config:
        SECRET_KEY = ":'("
        ...

        @classmethod
        def init_app(self, app)
            env = DotEnv()
            env.init_app(app)

            # this will be evaluated via ast.literal_eval
            env.eval(keys={
                MAIL_PORT: int
            })


Development
-----------

Run unittest.

::

    $ python setup.py test



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
