# Generated by Django 4.2.3 on 2023-07-28 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=128, unique=True)),
                ('product_id', models.IntegerField()),
                ('order_qty', models.IntegerField()),
                ('user_id', models.CharField(max_length=128, unique=True)),
                ('order_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=128, unique=True)),
                ('product_description', models.CharField(max_length=512, unique=True)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('product_stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=128, unique=True)),
                ('user_firstname', models.CharField(max_length=128, unique=True)),
                ('user_surname', models.CharField(max_length=128, unique=True)),
                ('user_email', models.CharField(max_length=128, unique=True)),
                ('user_orders', models.IntegerField()),
            ],
        ),
    ]
