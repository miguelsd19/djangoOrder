# Generated by Django 4.1.1 on 2022-09-12 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0002_remove_season_season'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='season',
            field=models.CharField(max_length=255, null=True),
        ),
    ]