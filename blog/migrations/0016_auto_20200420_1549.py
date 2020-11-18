# Generated by Django 3.0.3 on 2020-04-20 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200420_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.ImageField(default='categories.jpg', upload_to='Categories_icons'),
        ),
    ]