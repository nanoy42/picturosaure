Configuration
=============

There are two phases of configuration : the first one is related to django and the second one is specific to Picturosaure.

In the ``src/picturosaure`` folder there is file ``local_settings.example.py``. Copy it in the same directory as ``local_settings.py`` :


.. code-block:: bash

    cp src/picturosaure/local_settings.example.py src/picturosaure/local_settings.example.py


Django settings
###############

Please see the `django documentation <https://docs.djangoproject.com/fr/3.0/ref/settings>`_ for extended documentation.

.. attribute:: SECRET_KEY

Default: ``""``

A secret key for a particular Django installation. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value. This value should be kept secret.

.. warning::
    Django can't run without a secret key.

.. attribute:: DEBUG

Default: ``False``

A boolean that turns on/off debug mode. You should use ``DEBUG=False`` for production.

.. attribute:: ALLOWED_HOSTS

Default: ``[]``

A list of strings representing the host/domain names that this Django site can serve.

.. warning::
    Django can't run with ``DEBUG=False`` and ``ALLOWED_HOSTS=[]``.

.. attribute:: DATABASES

Default: ``{
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}``

If you use a postgresql database, on the same host as where you installed DinoMail, with the above values, it should look like this:

.. code-block:: python

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "dinomail",
            "USER": "dinomail",
            "PASSWORD": "secret",
            "HOST": "localhost",
        }
    }

    
.. attribute:: LANGUAGE_CODE

Default: ``"en-us"``

User will not be able to change the interface language. However, you can select the language you want from the listed below : 

 * English (``'en-us'``)
 * French (``'fr'``)

Those are the languages currently supported for DinoMail.

.. attribute:: TIME_ZONE

Default: ``"UTC"``

Time zone of the server.

.. attribute:: STATIC_ROOT

Default: ``BASE_DIR / "staticfiles"``

Folder in which the static files should be copied. You should make an alias for ``/static`` to this directory. 

.. attribute:: MEDIA_ROOT

Default: ``BASE_DIR / "media"``

Folder in which the media files should be uploaded. You should make an alias for ``/media`` to this directory. 


Picturosaure settings
#####################

There are some settings for picturosaure : 

.. attribute::PICTUROSAURE_USE_WATERMARK

Default : ``True``

If set to False, no watermark is added when the "add watermark" function is executed.

.. attribute::PICTUROSAURE_WATERMARK_POS

Default : ``"bottom-right"``

Position of the watermark. Should be one of the following : 

 * ``"top-left"``
 * ``"top-right"``
 * ``"bottom-left"``
 * ``"bottom-right"``

.. attribute:: PICTUROSAURE_WATERMARK_MARGIN

Default: ``20``

Margin to apply from the selected watermark position.

.. attribute:: PICTUROSAURE_WATERMARK_COLOR

Default : ``(255, 255, 255, 128)``

Color of the watermark in RGBA format (0-255).

.. attribute:: PICTUROSAURE_WATERMARK_SIZE

Default: ``100``

Size of the watermak.

.. attribute:: PICTUROSAURE_WATERMARK_TEXT

Default: ``"©"``

Text to print in the watermark.

.. attribute:: PICTUROSAURE_TITLE

Default: ``"Picturosaure"``

Text displayed in title.

.. attribute:: PICTUROSAURE_CONTACT

Default: ``"example@example.org"``

Contact email. If set to `""`, the mail icon is not displayed.

.. attribute:: PICTUROSAURE_LICENSE

Default: ``"""Where not stated otherwise, the photograph is distributed under 
the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank">CC BY-NC-SA 4.0</a> license (attribution to )."""``

The text is displayed on the right panel. Is supposed to give the default license of the pictures.

.. attribute:: PICTUROSAURE_LICENSE_NAME

Default: ``""``

Text to display right to the HTML5UP license information. If set to ``""`` nothing is displayed.