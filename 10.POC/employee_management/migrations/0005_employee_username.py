# Generated by Django 5.0.6 on 2024-05-10 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management', '0004_employee_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.CharField(default='ajay1616', max_length=255),
        ),
    ]