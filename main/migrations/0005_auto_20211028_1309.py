# Generated by Django 3.2.8 on 2021-10-28 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211028_1308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactformdata',
            options={},
        ),
        migrations.RemoveField(
            model_name='contactformdata',
            name='time',
        ),
    ]
