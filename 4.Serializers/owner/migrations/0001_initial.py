# Generated by Django 5.0.4 on 2024-05-04 06:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.CharField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('number', models.CharField(max_length=10, unique=True)),
                ('wing', models.CharField(default='D', max_length=100)),
                ('flat_no', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=255)),
                ('t_age', models.CharField()),
                ('t_email', models.EmailField(max_length=254, unique=True)),
                ('t_number', models.CharField(max_length=10, unique=True)),
                ('t_rent', models.BigIntegerField()),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.owner')),
            ],
        ),
    ]
