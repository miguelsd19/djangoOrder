# Generated by Django 4.1.1 on 2022-09-12 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderStatus', '0002_alter_orderstatus_ordernumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]