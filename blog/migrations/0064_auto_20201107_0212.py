# Generated by Django 3.0.3 on 2020-11-07 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0063_auto_20201107_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='post',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]