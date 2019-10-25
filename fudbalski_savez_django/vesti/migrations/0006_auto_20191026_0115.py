# Generated by Django 2.2.6 on 2019-10-25 23:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vesti', '0005_auto_20191025_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vesti',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='vesti_video', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]
