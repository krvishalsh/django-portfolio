# Generated by Django 3.2.8 on 2021-10-28 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_socialmedia_webdata_socialmedias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='image',
        ),
    ]