# Picturosaure - Hungry dino sharing pictures
# # Copyright (C) 2020 Yoann Piétri

# Picturosaure is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Picturosaure is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Picturosaure. If not, see <https://www.gnu.org/licenses/>.

########################### NOTICE ############################
###############################################################
# Please copy this file to src/picturosaure/local_settings.py #
# and fill it with appropriate values.                        #
# Note that this file is included at the end and can          #
# overwrite any django setting.                               #
###############################################################

from pathlib import Path

###################### Django settings ########################


BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SECRET_KEY = ""

DEBUG = False

ALLOWED_HOSTS = []


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_ROOT = BASE_DIR / "media"

PICTUROSAURE_USE_WATERMARK = True
PICTUROSAURE_WATERMARK_MARGIN = 20
PICTUROSAURE_WATERMARK_COLOR = (255, 2155, 255, 128)
PICTUROSAURE_WATERMARK_SIZE = 100
PICTUROSAURE_WATERMARK_TEXT = "© "
PICTUROSAURE_WATERMARK_POS = "bottom-right"
PICTUROSAURE_TITLE = "Picturosaure"
PICTUROSAURE_CONTACT = "example@example.org"
PICTUROSAURE_LICENSE = """
Where not stated otherwise, the photograph is distributed under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank">CC BY-NC-SA 4.0</a> license (attribution to ).
"""
PICTUROSAURE_LICENSE_NAME = ""
