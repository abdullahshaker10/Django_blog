# Generated by Django 3.0.3 on 2020-09-29 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20200929_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[(None, 'Select Your Gender type'), ('male', 'Male'), ('female', 'Female')], default='draft', max_length=10),
        ),
    ]
