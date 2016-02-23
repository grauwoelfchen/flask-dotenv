"""
FLask-DotEnv

:copyright: (c) 2015 by Yasuhiro Asaka.
:license: BSD 2-Clause License
"""

from __future__ import absolute_import
import ast
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
        if env_file is None:
            env_file = os.path.join(os.getcwd(), ".env")
        if not os.path.exists(env_file):
            warnings.warn("can't read {0} - it doesn't exist".format(env_file))
        else:
            self.__import_vars(env_file)

    def __import_vars(self, env_file):
        with open(env_file, "r") as f:
            for line in f:
                try:
                    key, value = line.strip().split('=', 1)
                except ValueError:  # Take care of blank or comment lines
                    pass
                try:
                    val = ast.literal_eval(value)
                    if self.verbose_mode:
                        print(" * {0}: value {1} of type {2} cast to {3}".format(key, value, type(value), type(val)))
                except (ValueError, SyntaxError):
                    if self.verbose_mode:
                        print(" * {0}: Couldn't evaluate syntax of value on .env line:\n     {1}\n"
                              "   Importing as string value.".format(key, line.strip()))
                    val = re.sub(r"\A[\"']|[\"']\Z", "", value)
                finally:
                    if not callable(val):
                        if self.verbose_mode:
                            if key in self.app.config:
                                msg = " * Overwriting an existing config var: {0}"
                            else:
                                msg = " * Setting an entirely new config var: {0}"
                            print(msg.format(key))
                        self.app.config[key] = val

    def alias(self, maps):
        for k, v in maps.items():
            if self.verbose_mode:
                print(
                    " * Mapping a specified var as a alias:"
                    " {0} => {1}".format(v, k)
                )
            self.app.config[v] = self.app.config[k]
