# Generated by Django 4.1.4 on 2023-02-08 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_products_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.RemoveField(
            model_name='products',
            name='stock',
        ),
    ]
