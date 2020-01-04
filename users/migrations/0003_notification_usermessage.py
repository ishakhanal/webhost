# Generated by Django 2.2.7 on 2019-12-12 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20191128_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usermessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_message', models.TextField()),
                ('admin_reply', models.TextField(blank=True)),
                ('send_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('message_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_message', models.TextField()),
                ('notification_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('message_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
