# Generated by Django 5.0.4 on 2024-05-02 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='doctor',
            new_name='doctor_id',
        ),
    ]
