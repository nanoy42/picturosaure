# Generated by Django 3.1 on 2020-08-30 21:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('url', models.URLField(verbose_name='url')),
                ('icon', models.CharField(max_length=255, verbose_name='icon')),
            ],
            options={
                'verbose_name': 'icon',
                'verbose_name_plural': 'icons',
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('url', models.URLField(verbose_name='url')),
            ],
            options={
                'verbose_name': 'license',
                'verbose_name_plural': 'licenses',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_initial', models.ImageField(upload_to='original', verbose_name='picture')),
                ('photo_watermark', models.ImageField(blank=True, upload_to='')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='description')),
                ('date', models.DateField(blank=True, null=True, verbose_name='date')),
                ('location', models.CharField(blank=True, max_length=255, verbose_name='location')),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.license')),
            ],
            options={
                'verbose_name': 'picture',
                'verbose_name_plural': 'pictures',
            },
        ),
    ]