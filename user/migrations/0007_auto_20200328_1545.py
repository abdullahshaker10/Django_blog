# Generated by Django 3.0.3 on 2020-03-28 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_profile_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friendrequest',
            old_name='user_from',
            new_name='from_user',
        ),
        migrations.RenameField(
            model_name='friendrequest',
            old_name='user_to',
            new_name='to_user',
        ),
    ]
