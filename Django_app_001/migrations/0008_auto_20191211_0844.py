# Generated by Django 2.2.7 on 2019-12-11 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Django_app_001', '0007_auto_20191211_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oprs_db',
            name='device_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='设备名'),
        ),
    ]
