# Generated by Django 2.2.6 on 2019-10-28 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vesti', '0004_auto_20191027_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vesti',
            name='video',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
