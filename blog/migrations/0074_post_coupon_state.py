# Generated by Django 3.0.3 on 2020-11-07 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0073_remove_post_coupon_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='coupon_state',
            field=models.BooleanField(default=False),
        ),
    ]
