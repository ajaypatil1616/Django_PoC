# Generated by Django 5.0.4 on 2024-05-03 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='language',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='style',
        ),
    ]
