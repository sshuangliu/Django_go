# Generated by Django 2.2.7 on 2019-12-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Django_app_001', '0002_auto_20191207_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='oprs_db',
            name='tips',
            field=models.TextField(blank=True, null=True),
        ),
    ]
