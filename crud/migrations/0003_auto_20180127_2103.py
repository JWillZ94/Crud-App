# Generated by Django 2.0.1 on 2018-01-28 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20180127_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('I do not wish to specify.', 'I do not wish to specify.'), ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20),
        ),
    ]
