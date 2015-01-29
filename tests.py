import os
import unittest
import warnings
import flask

import flask_dotenv as dotenv


class ReadEnvFileTestCase(unittest.TestCase):
    def setUp(self):
        self.app = flask.Flask(__name__)
        self.env = dotenv.DotEnv()

    def tearDown(self):
        if os.environ.get('DOTENV', None):
            del os.environ['DOTENV']

    def test_warning_if_env_file_is_missing(self):
        with warnings.catch_warnings(record=True) as w:
            self.env.init_app(self.app, "/does/not/exist/.env")
            self.assertEqual(
                str(w[0].message),
                "can't read /does/not/exist/.env - it doesn't exist"
            )
        self.assertEqual(os.environ.get('DOTENV'), None)

    def test_read_default_env_file(self):
        self.env.init_app(self.app)
        self.assertEqual(os.environ.get('DOTENV'), 'true')

    def test_read_specified_env_file(self):
        self.env.init_app(self.app, ".env")
        self.assertEqual(os.environ.get('DOTENV'), 'true')


if __name__ == '__main__':
    unittest.main()
