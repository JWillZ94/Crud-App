# Generated by Django 2.0.1 on 2018-02-12 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20180211_0219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
