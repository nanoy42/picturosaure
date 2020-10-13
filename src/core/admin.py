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

from django.contrib import admin

from . import models


def make_watermark(modeladmin, request, queryset):
    """Add watermark to every element in the queryset.

    Args:
        modeladmin (ModelAdmin): modeladmin when the action was triggered (here PhotoAdmin).
        request (HttpRequest): django http request.
        queryset (Queryset): queryset on which to apply the action.
    """
    for photo in queryset:
        photo.add_watermark()


make_watermark.short_description = "Generate watermark for selected images"


class IconAdmin(admin.ModelAdmin):
    """Admin class for Icon.
    """

    list_display = ["name", "icon", "url"]


class LicenseAdmin(admin.ModelAdmin):
    """Admin class for License.
    """

    list_display = ["name", "url"]


class PhotoAdmin(admin.ModelAdmin):
    """Admin class for Photo.
    """

    list_display = [
        "name",
        "date",
        "location",
        "license",
        "photo_initial",
        "photo_watermark",
    ]
    ordering = ["name"]
    actions = [make_watermark]
    fields = [
        "name",
        "photo_initial",
        "license",
        "description",
        "date",
        "location",
    ]


admin.site.register(models.Icon, IconAdmin)
admin.site.register(models.License, LicenseAdmin)
admin.site.register(models.Photo, PhotoAdmin)
