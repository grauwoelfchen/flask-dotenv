"""
Flask-DotEnv
------------

The .env file support for Flask without os.environ dependency.
"""

from setuptools import setup


setup(
    name='Flask-DotEnv',
    version='0.1.1',
    url='https://github.com/grauwoelfchen/flask-dotenv/',
    license='BSD',
    author='Yasuhiro Asaka',
    author_email='grauwoelfchen@gmail.com',
    description='The .env file support for Flask',
    long_description=__doc__,
    py_modules=['flask_dotenv'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    test_suite='tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Software Distribution'
    ]
)
