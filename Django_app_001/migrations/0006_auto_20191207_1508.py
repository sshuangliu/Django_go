# Generated by Django 2.2.7 on 2019-12-07 15:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Django_app_001', '0005_auto_20191207_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oprs_db',
            name='device_sn',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='SN must be ....', regex='^\\d*$')]),
        ),
    ]