"""
FLask-DotEnv

:copyright: (c) 2015 by Yasuhiro Asaka.
:license: BSD 2-Clause License
"""

import os
import re
import warnings


class DotEnv(object):
    """The .env file support for Flask."""

    def __init__(self, app=None):
        self.app = app
        self.verbose_mode = False
        if app is not None:
            self.init_app(app)

    def init_app(self, app, env_file=None, verbose_mode=False):
        if self.app is None:
            self.app = app
        self.verbose_mode = verbose_mode

        if env_file is None:
            env_file = os.path.join(os.getcwd(), ".env")
        if not os.path.exists(env_file):
            warnings.warn("can't read {0} - it doesn't exist".format(env_file))
        else:
            self.__import_vars(env_file)

    def __import_vars(self, env_file):
        with open(env_file, "r") as f:
            for line in f:
                key, val = line.strip().split('=')
                if not callable(val):
                    if self.verbose_mode:
                        if key in self.app.config:
                            msg = " * Overwriting an existing config var: {0}"
                        else:
                            msg = " * Setting an entirely new config var: {0}"
                        print(msg.format(key))
                    self.app.config[key] = re.sub(r"\A[\"']|[\"']\Z", "", val)

    def alias(self, maps):
        for k, v in maps.items():
            if self.verbose_mode:
                print(
                    " * Mapping a specified var as a alias:"
                    " {0} => {1}".format(v, k)
                )
            self.app.config[v] = self.app.config[k]
