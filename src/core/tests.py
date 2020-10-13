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
Tests for picturosaure.
"""

import base64
import os
import tempfile
from io import BytesIO
from pathlib import Path

from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.test import Client, TestCase, override_settings

from .models import Icon, License, Photo


class IconTestCase(TestCase):
    """Test case for icons
    """

    def setUp(self):
        """Set up the tests
        """
        self.icon = Icon.objects.create(
            name="GitHub",
            icon="fab fa-github",
            url="https://github.com/nanoy42/picturosaure",
        )

    def test_str(self):
        self.assertEqual(str(self.icon), "GitHub")


class LicenseTestCase(TestCase):
    """Test case for licenses
    """

    def setUp(self):
        self.license = License.objects.create(
            name="CC BY-NC-SA 4.0",
            url="https://creativecommons.org/licenses/by-nc-sa/4.0/",
        )

    def test_str(self):
        self.assertEqual(str(self.license), "CC BY-NC-SA 4.0")


class PhotoTestCase(TestCase):
    """Test case for photos
    """

    TEST_IMAGE = """
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
""".strip()

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def setUp(self):
        self.license = License.objects.create(
            name="CC BY-NC-SA 4.0",
            url="https://creativecommons.org/licenses/by-nc-sa/4.0/",
        )
        image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(self.TEST_IMAGE)),
            field_name="tempfile",
            name="tempfile.png",
            content_type="image/png",
            size=len(self.TEST_IMAGE),
            charset="utf-8",
        )
        self.photo = Photo.objects.create(
            name="test", license=self.license, photo_initial=image
        )
        self.c = Client()
        self.password = "password"
        self.superuser = User.objects.create_superuser(
            "superuser", "test@example.com", self.password
        )

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_str(self):
        self.assertEqual(str(self.photo), "test")

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    @override_settings(PICTUROSAURE_WATERMARK_POS="bottom-right")
    def test_watermark(self):
        self.assertEqual(self.photo.photo_watermark.name, "")
        self.photo.add_watermark()
        self.assertNotEqual(self.photo.photo_watermark.name, "")

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    @override_settings(PICTUROSAURE_WATERMARK_POS="top-right")
    def test_watermark_top_right(self):
        self.assertEqual(self.photo.photo_watermark.name, "")
        self.photo.add_watermark()
        self.assertNotEqual(self.photo.photo_watermark.name, "")

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    @override_settings(PICTUROSAURE_WATERMARK_POS="top-left")
    def test_watermark_top_left(self):
        self.assertEqual(self.photo.photo_watermark.name, "")
        self.photo.add_watermark()
        self.assertNotEqual(self.photo.photo_watermark.name, "")

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    @override_settings(PICTUROSAURE_WATERMARK_POS="bottom-left")
    def test_watermark_bottom_left(self):
        self.assertEqual(self.photo.photo_watermark.name, "")
        self.photo.add_watermark()
        self.assertNotEqual(self.photo.photo_watermark.name, "")

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_readd_watermark(self):
        self.photo.add_watermark()
        self.photo.add_watermark()

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_make_watermark(self):
        self.assertEqual(self.photo.photo_watermark.name, "")
        self.c.login(username=self.superuser.username, password=self.password)
        data = {
            "action": "make_watermark",
            "_selected_action": [self.photo.pk],
        }
        response = self.c.post("/admin/core/photo/", data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.photo = Photo.objects.get(pk=self.photo.pk)
        self.assertNotEqual(self.photo.photo_watermark.name, "")

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_delete(self):
        self.assertTrue(os.path.isfile(self.photo.photo_initial.path))
        self.photo.delete()
        self.assertFalse(os.path.isfile(self.photo.photo_initial.path))

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_delete_with_matermark(self):
        self.photo.add_watermark()
        self.assertTrue(os.path.isfile(self.photo.photo_initial.path))
        self.assertTrue(os.path.isfile(self.photo.photo_watermark.path))
        self.photo.delete()
        self.assertFalse(os.path.isfile(self.photo.photo_initial.path))
        self.assertFalse(os.path.isfile(self.photo.photo_watermark.path))

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_change(self):
        image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(self.TEST_IMAGE)),
            field_name="tempfile",
            name="tempfile2.png",
            content_type="image/png",
            size=len(self.TEST_IMAGE),
            charset="utf-8",
        )
        path = self.photo.photo_initial.path
        self.photo.photo_initial = image
        self.photo.save()
        self.assertTrue(os.path.isfile(self.photo.photo_initial.path))
        self.assertFalse(os.path.isfile(path))

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_change_with_watermark(self):
        self.photo.add_watermark()
        image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(self.TEST_IMAGE)),
            field_name="tempfile",
            name="tempfile2.png",
            content_type="image/png",
            size=len(self.TEST_IMAGE),
            charset="utf-8",
        )
        path = self.photo.photo_watermark.path
        self.photo.photo_initial = image
        self.photo.save()
        self.assertFalse(os.path.isfile(path))


class ViewsTestCase(TestCase):
    """Test for views.
    """

    def setUp(self):
        """Set up the tests.
        """
        self.c = Client()

    def test_home(self):
        """Test the home view.
        """
        response = self.c.get("/")
        self.assertEquals(response.status_code, 200)
