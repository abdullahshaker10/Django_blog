# Generated by Django 3.0.3 on 2020-05-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_post_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
