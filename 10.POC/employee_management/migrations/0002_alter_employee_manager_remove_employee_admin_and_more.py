# Generated by Django 5.0.6 on 2024-05-09 08:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='employee',
            name='admin',
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
    ]
