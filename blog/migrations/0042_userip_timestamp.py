# Generated by Django 3.1.1 on 2020-09-25 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0041_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='userip',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]