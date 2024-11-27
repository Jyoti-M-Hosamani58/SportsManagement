# Generated by Django 3.0 on 2024-11-24 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports_app', '0002_auto_20241122_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='inncreaseStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kit_name', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=255)),
                ('price_per_unit', models.CharField(max_length=255)),
                ('total_cost', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
            ],
        ),
    ]
