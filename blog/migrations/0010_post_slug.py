# Generated by Django 3.0.3 on 2020-04-20 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, unique_for_date='post_publish'),
        ),
    ]
