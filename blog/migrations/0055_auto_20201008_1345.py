# Generated by Django 3.0.3 on 2020-10-08 11:45

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0054_coupon_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(default=blog.models.get_random_code, editable=False, max_length=8, unique=False, verbose_name='Coupon Code'),
        ),
    ]
