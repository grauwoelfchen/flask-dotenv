Flask-DotEnv
------------

.. image:: https://travis-ci.org/grauwoelfchen/flask-dotenv.svg?branch=master
    :target: https://travis-ci.org/grauwoelfchen/flask-dotenv

.. image:: https://img.shields.io/pypi/v/Flask-Dotenv.svg
    :target: https://pypi.python.org/pypi/Flask-Dotenv/

| Adds support for the ``.env`` file to flask style config class for applications.
| Version ``0.0.3`` and above support setting config variables without using ``os.environ``.
|


``Flask-DotEnv`` will directly set (add, update, map as alias and eval as
literal) variables from ``.env`` file, and cast them to Python native types
as appropriate.

(optional)

* ``alias()`` makes alias vars
* ``eval()`` evaluate var to literal (via ``ast``)


Repositories
------------

| My main repository is on GitLab (.com). 
| But pull requests on GitHub are also welcome. :-D

* https://gitlab.com/grauwoelfchen/flask-dotenv.git (main)
* https://github.com/grauwoelfchen/flask-dotenv.git



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
    from flask_dotenv import DotEnv

    app = Flask(__name__)
    env = DotEnv(app)

As a factory pattern.

::

    env = DotEnv()
    env.init_app(app)

| This ``env`` module may be useful in your Config class.
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

    from config import Config

    app = Flask(__name__)
    app.config.from_object(config[config_name])

See also:

`flask.Config.from_object <http://flask.pocoo.org/docs/1.0/api/#flask.Config.from_object>`_ (Flask's API documentation)

**********
Arguments
**********

You can pass the ``.env`` file path as a second argument of ``init_app()``.

::

    env.init_app(app, env_file="/path/to/.env", verbose_mode=True)

| The second argument (``env_file``) is optional, and the default is ``os.path.join(os.getcwd(), '.env')``.
| The third argument (``verbose_mode``) is also optional, and defaults to ``False``.

| If ``verbose_mode`` is ``True``, then server outputs nice log message showing which vars will be set,
| like this:

::

    * Overwriting an existing config var: SECRET_KEY
    * Setting an entirely new config var: DEVELOPMENT_DATABASE_URL
    * Casting a denoted var as a literal: MAIL_PORT => <class 'int'>
    * Making a specified var as an alias: DEVELOPMENT_DATABASE_URL -> SQLALCHEMY_DATABASE_URI
    ...

**********
Alias
**********

The ``alias()`` method takes a dict argument. Each key is the existing config var,
while each value is the new alias.

::

    env.alias(maps={
      'TEST_DATABASE_URL': 'SQLALCHEMY_DATABASE_URI',
      'TEST_HOST': 'HOST'
    })

Here's an example of its use:

::

    class Config:
        SECRET_KEY = ":'("
        ...

        @classmethod
        def init_app(self, app)
            env = DotEnv()
            env.init_app(app)

            # The following will store in `SQLALCHEMY_DATABASE_URI` the value
            # in, for example, `DEVELOPMENT_DATABASE_URL`
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

``eval()`` also takes a dict argument. These keys are also the existing config
var, while the values are the type they should evaluate to. If the type is
something else, the config var is skipped with a log message shown.

::

    env.eval(keys={
      'MAIL_PORT': int,
      'SETTINGS': dict
    })

And here's an example of its use:

::

    class Config:
        SECRET_KEY = ":'("
        ...

        @classmethod
        def init_app(self, app)
            env = DotEnv()
            env.init_app(app)

            # `MAIL_PORT` will be set the the integer verson of the value found there
            # using `ast.literal_eval`.
            env.eval(keys={
                MAIL_PORT: int
            })



.env File
-----------

The following lines are all valid.

::

    SECRET_KEY="123"
    USERNAME=john
    DATABASE_URL='postgresql://user:password@localhost/production?sslmode=require'
    FEATURES={'DotEnv': True}
    # comment and blank lines are also supported

    export ENV="production"
    export env="staging"



Development
-----------

Run the unit tests with:

::

    $ python setup.py test



Link
----

Inspired by:

* `python-dotenv`_
* `django-dotenv`_

Other packages that also set configuration variables:

* `Flask-EnvConfig`_
* `Flask-UserEnvConfig`_


License
-------

BSD 2-Clause License


.. _python-dotenv: https://github.com/theskumar/python-dotenv
.. _django-dotenv: https://github.com/jpadilla/django-dotenv
.. _Flask-EnvConfig: https://bitbucket.org/romabysen/flask-envconfig
.. _Flask-UserEnvConfig: https://github.com/caustin/flask-userenvconfig
