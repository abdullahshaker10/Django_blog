# Generated by Django 3.0.3 on 2020-04-20 10:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
