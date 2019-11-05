# Generated by Django 2.2.6 on 2019-11-05 14:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delegat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=20)),
                ('prezime', models.CharField(max_length=20)),
                ('datum_rodjenja', models.DateField(blank=True, null=True)),
                ('zvanje', models.CharField(max_length=200, null=True)),
                ('slika', models.ImageField(default='sudija.jpg', upload_to='delegat_img')),
            ],
            options={
                'verbose_name_plural': 'Delegati',
            },
        ),
        migrations.CreateModel(
            name='Sezona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sezona', models.PositiveSmallIntegerField()),
                ('tip', models.CharField(max_length=30)),
            ],
            options={
                'unique_together': {('sezona', 'tip')},
            },
        ),
        migrations.CreateModel(
            name='Sudija',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=20)),
                ('prezime', models.CharField(max_length=20)),
                ('zvanje', models.CharField(max_length=200, null=True)),
                ('datum_rodjenja', models.DateField(blank=True, null=True)),
                ('slika', models.ImageField(default='sudija.jpg', upload_to='delegat_img')),
            ],
            options={
                'verbose_name_plural': 'Sudije',
            },
        ),
        migrations.CreateModel(
            name='Tim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Timovi',
            },
        ),
        migrations.CreateModel(
            name='TimoviSokobanja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=30)),
                ('ucesce', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='logo_img')),
            ],
            options={
                'verbose_name_plural': 'TimoviSokobanje',
            },
        ),
        migrations.CreateModel(
            name='Utakmica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kolo', models.PositiveSmallIntegerField()),
                ('domacin_gol', models.PositiveSmallIntegerField(default=0)),
                ('gost_gol', models.PositiveSmallIntegerField(default=0)),
                ('mesto_odigravanja', models.CharField(max_length=100)),
                ('datum_zakazano', models.DateTimeField(default=django.utils.timezone.now)),
                ('datum_odigrano', models.DateTimeField(default=django.utils.timezone.now)),
                ('delegat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='delegat', to='fudbal.Delegat')),
                ('domacin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domacin', to='fudbal.TimoviSokobanja')),
                ('drugi_pomocnik', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='drug_pomocnik', to='fudbal.Sudija')),
                ('glavni_sudija', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='glavni_sudija', to='fudbal.Sudija')),
                ('gost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gost', to='fudbal.TimoviSokobanja')),
                ('prvi_pomocnik', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='prvi_pomocnik', to='fudbal.Sudija')),
                ('sezona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fudbal.Sezona')),
            ],
            options={
                'verbose_name_plural': 'Utakmice',
            },
        ),
        migrations.CreateModel(
            name='TimSezona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aktivan', models.BooleanField(default=True)),
                ('sezona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fudbal.Sezona')),
                ('tim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fudbal.TimoviSokobanja')),
            ],
        ),
        migrations.CreateModel(
            name='Kazne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kazneni_bodovi', models.PositiveSmallIntegerField()),
                ('razlog', models.TextField()),
                ('datum', models.DateField()),
                ('tim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fudbal.TimSezona')),
            ],
        ),
    ]
