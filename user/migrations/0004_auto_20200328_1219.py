# Generated by Django 3.0.3 on 2020-03-28 10:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_auto_20200328_1207'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='FriendRequest',
        ),
    ]