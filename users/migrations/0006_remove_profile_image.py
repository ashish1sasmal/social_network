# Generated by Django 2.1 on 2019-09-08 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]
