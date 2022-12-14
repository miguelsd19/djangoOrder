# Generated by Django 4.1.1 on 2022-09-11 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderNumber', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('SHIPPED', 'SHIPPED'), ('PENDING', 'PENDING'), ('CANCELLED', 'CANCELLED')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('SHIPPED', 'SHIPPED'), ('PENDING', 'PENDING'), ('CANCELLED', 'CANCELLED')], max_length=255)),
                ('OrderNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='OrderStatus.orderstatus')),
            ],
        ),
    ]
