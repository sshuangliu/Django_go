# Generated by Django 2.2.7 on 2019-12-07 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Django_app_001', '0004_auto_20191207_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oprs_db',
            name='mail',
            field=models.EmailField(max_length=100, verbose_name='厂家联系邮件'),
        ),
    ]
