# Generated by Django 3.0.3 on 2020-08-14 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_remove_profile_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='title',
        ),
    ]
