# Generated by Django 4.1.1 on 2022-09-12 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='season',
        ),
    ]
