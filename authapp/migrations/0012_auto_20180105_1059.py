# Generated by Django 2.0 on 2018-01-05 05:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0011_auto_20171227_0101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 7, 5, 59, 47, 919766, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
