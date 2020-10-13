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
Models for picturosaure.
"""

import os

from django.conf import settings
from django.core.files import File
from django.db import models
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from PIL import Image, ImageDraw, ImageFont


class Icon(models.Model):
    """Icon model.
    
    Each icon is displayed on the panel on the home page.

    Args:
        name (string): name of the icon
        url (string): link to go when the icon is clicked
        icon (string): font awesome cion to display
    """

    class Meta:
        verbose_name = _("icon")
        verbose_name_plural = _("icons")

    name = models.CharField(max_length=255, verbose_name=_("name"))
    url = models.URLField(verbose_name=_("url"))
    icon = models.CharField(max_length=255, verbose_name=_("icon"))

    def __str__(self):
        """str method for icons

        Returns:
            string: return the name of the icon.
        """
        return self.name


class License(models.Model):
    """License model.

    Pictures are linked to a license object.

    Args:
        name (string): name of the license
        url (string): where to find the full license text
    """

    class Meta:
        verbose_name = _("license")
        verbose_name_plural = _("licenses")

    name = models.CharField(max_length=255, verbose_name=_("name"))
    url = models.URLField(verbose_name=_("url"))

    def __str__(self):
        """str method for licenses.

        Returns:
            string: return name of the license.
        """
        return self.name


class Photo(models.Model):
    """Photo model.

    Args:
        photo_initial (image): image field corresponding to the initial picture.
        photo_watermark (image): image field corresponding to the picture with watermark.
        name (string): name of the picture.
        description (string): description of the picture.
        date (string): date of the picture.
        location (string): location of the picture
        license (License): license object.
    """

    class Meta:
        verbose_name = _("picture")
        verbose_name_plural = _("pictures")

    photo_initial = models.ImageField(verbose_name=_("picture"), upload_to="original")
    photo_watermark = models.ImageField(blank=True)
    name = models.CharField(max_length=255, verbose_name=_("name"), blank=False)
    description = models.CharField(
        max_length=255, verbose_name=_("description"), blank=True
    )
    date = models.DateField(blank=True, null=True, verbose_name=_("date"))
    location = models.CharField(max_length=255, blank=True, verbose_name=_("location"))
    license = models.ForeignKey(License, on_delete=models.PROTECT)

    def __str__(self):
        """str method for photos.

        Returns:
            string: name of the photo.
        """
        return self.name

    def add_watermark(self):
        """Add watermark to the initial picture.

        The watermark to add is stored into the WATERMARK_TEXT settings.
        Watermark size and margin ar stored into WATERMARK_SIZE and WATERMARK_MARGIN settings.
        If USE_WATERMARK is set to False, no watermark is added but the initial photo is copied to photo_watermark.
        """
        if self.photo_watermark:
            if os.path.isfile(self.photo_watermark.path):
                os.remove(self.photo_watermark.path)
        photo = Image.open(self.photo_initial.path).convert("RGBA")
        txt = Image.new("RGBA", photo.size, (255, 255, 255, 0))
        drawing = ImageDraw.Draw(txt)
        font = ImageFont.truetype(
            str(settings.STATIC_ROOT / "arial.ttf"),
            settings.PICTUROSAURE_WATERMARK_SIZE,
        )
        text_w, text_h = drawing.textsize(settings.PICTUROSAURE_WATERMARK_TEXT, font)
        width, height = photo.size
        if settings.PICTUROSAURE_USE_WATERMARK:
            if settings.PICTUROSAURE_WATERMARK_POS == "top-left":
                x = settings.PICTUROSAURE_WATERMARK_MARGIN
                y = settings.PICTUROSAURE_WATERMARK_MARGIN
            elif settings.PICTUROSAURE_WATERMARK_POS == "top-right":
                x = width - text_w - settings.PICTUROSAURE_WATERMARK_MARGIN
                y = settings.PICTUROSAURE_WATERMARK_MARGIN
            elif settings.PICTUROSAURE_WATERMARK_POS == "bottom-left":
                x = settings.PICTUROSAURE_WATERMARK_MARGIN
                y = height - text_h - settings.PICTUROSAURE_WATERMARK_MARGIN
            else:
                # Default is bottom-right
                x = width - text_w - settings.PICTUROSAURE_WATERMARK_MARGIN
                y = height - text_h - settings.PICTUROSAURE_WATERMARK_MARGIN
            drawing.text(
                (x, y,),
                settings.PICTUROSAURE_WATERMARK_TEXT,
                fill=settings.PICTUROSAURE_WATERMARK_COLOR,
                font=font,
            )
        out = Image.alpha_composite(photo, txt)
        out.save(
            "{}/media/watermark/{}.png".format(
                settings.BASE_DIR, self.photo_initial.name.split("/")[-1].split(".")[0]
            )
        )
        self.photo_watermark.save(
            "watermark/{}".format(self.photo_initial.name.split("/")[-1]),
            File(
                open(
                    "{}/media/watermark/{}.png".format(
                        settings.BASE_DIR,
                        self.photo_initial.name.split("/")[-1].split(".")[0],
                    ),
                    "rb",
                )
            ),
        )
        os.remove(
            "{}/media/watermark/{}.png".format(
                settings.BASE_DIR, self.photo_initial.name.split("/")[-1].split(".")[0]
            )
        )


@receiver(models.signals.post_delete, sender=Photo)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Signal to delete files when instance is deleted

    Args:
        sender (Model): Model that trigerred the signal. Here : Photo
        instance (Photo): Photo that triggered the signal.
    """
    if instance.photo_initial:
        if os.path.isfile(instance.photo_initial.path):
            os.remove(instance.photo_initial.path)
    if instance.photo_watermark:
        if os.path.isfile(instance.photo_watermark.path):
            os.remove(instance.photo_watermark.path)


@receiver(models.signals.pre_save, sender=Photo)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """Signal to delete files when instanc eis changed, if needed

    Args:
        sender (Model): Model that triggered the signal. Here : Photo
        instance (Photo): Photo that triggered the signal.

    Returns:
        bool: return False if it is a creation.
    """
    if not instance.pk:
        return False

    photo = Photo.objects.get(pk=instance.pk)

    old_file = photo.photo_initial
    if photo.photo_watermark.name:
        old_watermark = photo.photo_watermark
    else:
        old_watermark = None

    new_file = instance.photo_initial
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
        if old_watermark and os.path.isfile(old_watermark.path):
            os.remove(old_watermark.path)
