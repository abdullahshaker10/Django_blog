# Generated by Django 3.0.3 on 2020-10-25 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_profile_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='account_balance',
        ),
        migrations.DeleteModel(
            name='MakeDeposit',
        ),
    ]
