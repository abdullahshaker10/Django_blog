# Generated by Django 3.0.3 on 2020-09-29 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_remove_profile_taxes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[(None, 'Select Your Gender type'), ('male', 'Male'), ('female', 'Female')], default='male', max_length=10),
        ),
    ]