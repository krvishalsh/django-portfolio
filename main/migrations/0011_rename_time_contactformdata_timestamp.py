# Generated by Django 3.2.8 on 2021-10-28 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_contactformdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactformdata',
            old_name='time',
            new_name='timestamp',
        ),
    ]