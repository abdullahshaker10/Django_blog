# Generated by Django 3.1.1 on 2020-09-25 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0044_userip_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userip',
            name='post',
        ),
        migrations.AddField(
            model_name='userip',
            name='post',
            field=models.ManyToManyField(blank=True, null=True, related_name='ipp_post', to='blog.Post'),
        ),
    ]
