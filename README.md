# Picturosaure

[![Documentation Status](https://readthedocs.org/projects/picturosaure/badge/?version=latest)](https://picturosaure.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/nanoy42/picturosaure/badge.svg?branch=master)](https://coveralls.io/github/nanoy42/picturosaure?branch=master)
[![github-actions](https://github.com/nanoy42/picturosaure/workflows/Django%20CI/badge.svg)](https://github.com/nanoy42/picturosaure/workflows/Django%20CI)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Code style black](https://img.shields.io/badge/code%20style-black-000000.svg)]("https://github.com/psf/black)
[![GitHub release](https://img.shields.io/github/release/nanoy42/picturosaure.svg)](https://github.com/nanoy42/picturosaure/releases/)

Picturosaure is a nice Dino helping you to share your pictures.

It is a simple Django app to share your picutres, with watermarks.

Summary :

 * [Functionalities](#functionalities)
 * [Supported languages](#supported-languages)
 * [Documentation](#documentation)
 * [Screenshots](#screenshots)
 * [License](#license)
 * [Tests and dev](#tests-and-dev)

Credits to zaiken for the logo.

## Functionalities

 * Upload pictures and display them in a nice way
 * Link pictures to licenses
 * Add description, location and date to pictures
 * Automatically add watermarks to pictures
 * Add social icons and links

## Supported languages

The following languages are supported :

 * English (`en-us`)
 * French (`fr`)

## Documentation

The full documentation ca be found at https://picturosaure.readthedocs.io/en/latest/.

## Screenshots

![home](https://github.com/nanoy42/picturosaure/raw/master/res/screenshots/home.png "Home page")

## License

Picturosaure is distributed under the GPLv3 license :

Picturosaure - Hungry dino sharing pictures
Copyright (C) 2020 Yoann Piétri

Picturosaure is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Picturosaure is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Picturosaure. If not, see <https://www.gnu.org/licenses/>.


## Tests and dev

You can run install the dev dependencies with 

```
pipenv install --dev
```

or 

```
pip3 install -r dev-requirements.txt
```

You can run the test with 

```
python3 manage.py test
```