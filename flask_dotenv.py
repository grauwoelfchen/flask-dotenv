"""
FLask-DotEnv

:copyright: (c) 2015 by Yasuhiro Asaka.
:license: BSD 2-Clause License
"""

import os
import warnings
import dotenv


class DotEnv(object):
    """The .env file support for Flask."""

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app, env_file=None):
        if env_file is None:
            env_file = os.path.join(os.getcwd(), '.env')
        if not os.path.exists(env_file):
            warnings.warn("can't read {0} - it doesn't exist".format(env_file))
        else:
            dotenv.load_dotenv(env_file)
