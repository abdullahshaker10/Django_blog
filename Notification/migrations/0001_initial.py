# Generated by Django 3.0.3 on 2020-11-09 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(default='NO description', max_length=50)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('is_resd', models.BooleanField(default=False)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
