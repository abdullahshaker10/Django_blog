# Generated by Django 3.0.3 on 2020-09-08 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_remove_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating01',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='rating02',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='rating03',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='rating04',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
    ]