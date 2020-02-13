# Quart-JWT-Extended
[![Build Status](https://travis-ci.org/greenape/quart-jwt-extended.svg?branch=master)](https://travis-ci.org/greenape/quart-jwt-extended)
[![Coverage Status](https://coveralls.io/repos/github/greenape/quart-jwt-extended/badge.svg?branch=master)](https://coveralls.io/github/greenape/quart-jwt-extended?branch=master)
[![PyPI version](https://badge.fury.io/py/Quart-JWT-Extended.svg)](https://badge.fury.io/py/Quart-JWT-Extended)
[![Documentation Status](https://readthedocs.org/projects/quart-jwt-extended/badge/)](http://quart-jwt-extended.readthedocs.io/en/latest/)

Quart-JWT-Extended is an async fork of the excellent [Flask-JWT-Extended](https://github.com/vimalloc/flask-jwt-extended) for use with [Quart](https://pgjones.gitlab.io/quart/)

### Features
Quart-JWT-Extended not only adds support for using JSON Web Tokens (JWT) to Quart for protecting views,
but also many helpful (and **optional**) features  built in to make working with JSON Web Tokens
easier. These include:

* Support for adding custom claims to JSON Web Tokens
* Custom claims validation on received tokens
* Creating tokens from complex objects or complex object from received tokens
* [Refresh tokens](https://auth0.com/blog/refresh-tokens-what-are-they-and-when-to-use-them/)
* Token freshness and separate view decorators to only allow fresh tokens
* Token revoking/blacklisting
* Storing tokens in cookies and CSRF protection

### Usage
[View the documentation online](https://quart-jwt-extended.readthedocs.io/en/stable/)

### Changelog
You can view the changelog [here](https://github.com/greenape/quart-jwt-extended/releases).
This project follows [semantic versioning](https://semver.org/).

### Local Development
We require 100% code coverage in our unit tests. You can run the tests locally
with `tox` which will print out a code coverage report. Creating a pull request
will run the tests against python 3.7 and 3.8.
```
$ tox
```

We also require features to be well documented. After installing the requirements,
you can generate a local copy of documentation by going to the `docs` directory
and running:
```
$ make clean && make html
```
