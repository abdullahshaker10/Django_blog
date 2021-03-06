# Generated by Django 3.0.3 on 2020-10-05 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0049_favoritespost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='couponorder',
            options={'ordering': ('-created_at',), 'verbose_name': 'coupon_orders', 'verbose_name_plural': 'Coupon Orders'},
        ),
        migrations.AddField(
            model_name='wishlist',
            name='favpost',
            field=models.ManyToManyField(blank=True, related_name='favoritepost', to='blog.Post'),
        ),
        migrations.DeleteModel(
            name='FavoritesPost',
        ),
    ]
