# Generated by Django 3.0.3 on 2020-10-08 11:44

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0053_remove_coupon_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='code',
            field=models.CharField(default=blog.models.get_random_code, editable=False, max_length=8, unique=False, verbose_name='Coupon Code'),
        ),
    ]
