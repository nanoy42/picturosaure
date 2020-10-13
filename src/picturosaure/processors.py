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

"""
Cutsom processor for Picturosaure.
"""
from django.conf import settings


def conf_processor(request):
    """Setting processors.
    This processor let the templates have access to some chosen variables of the settings.
    Args:
        request (HttpRequest): django request object.
    Returns:
        dict: context with the chosen values.
    """
    return {
        "PICTUROSAURE_TITLE": settings.PICTUROSAURE_TITLE,
        "PICTUROSAURE_CONTACT": settings.PICTUROSAURE_CONTACT,
        "PICTUROSAURE_LICENSE": settings.PICTUROSAURE_LICENSE,
        "PICTUROSAURE_LICENSE_NAME": settings.PICTUROSAURE_LICENSE_NAME,
    }
