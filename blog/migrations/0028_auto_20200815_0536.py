# Generated by Django 3.0.3 on 2020-08-15 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20200515_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='favourite',
            new_name='favorites',
        ),
    ]
