# Generated by Django 5.1.5 on 2025-02-16 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DPDM2', '0002_camp_login_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='public',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DPDM2.login')),
            ],
        ),
        migrations.CreateModel(
            name='station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.CharField(max_length=50)),
                ('address_line1', models.CharField(max_length=100)),
                ('address_line2', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
                ('authentication', models.IntegerField()),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DPDM2.login')),
            ],
        ),
        migrations.CreateModel(
            name='volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('contact', models.CharField(max_length=10)),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DPDM2.login')),
            ],
        ),
    ]
