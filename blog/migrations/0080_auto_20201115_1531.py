# Generated by Django 3.0.3 on 2020-11-15 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0079_order_final_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(default='Pending', max_length=10),
        ),
    ]
