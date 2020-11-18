# Generated by Django 3.0.3 on 2020-09-29 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0012_remove_profile_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='account_balance',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='current_balance'),
        ),
        migrations.AddField(
            model_name='profile',
            name='taxes',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='user_taxes'),
        ),
        migrations.CreateModel(
            name='MakeDeposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('date_deposited', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('DENIED', 'Denied')], default='Approved', max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]