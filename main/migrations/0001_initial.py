# Generated by Django 3.2.8 on 2021-10-28 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=256)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('percentage', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='skills')),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('link', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='WebData',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('short_descr', models.CharField(max_length=100)),
                ('med_descr', models.CharField(max_length=200)),
                ('long_descr', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('status', models.CharField(max_length=32)),
                ('skills', models.ManyToManyField(blank=True, to='main.Skill')),
                ('socialmedia', models.ManyToManyField(blank=True, to='main.SocialMedia')),
            ],
        ),
    ]