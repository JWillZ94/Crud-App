# Generated by Django 2.0.1 on 2018-01-28 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_auto_20180127_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.CharField(default='12345678', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
