# Generated by Django 3.0.3 on 2020-08-21 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_auto_20200821_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='blog.Tag'),
        ),
    ]
