# Generated by Django 5.0.2 on 2024-03-02 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_remove_item_image_remove_item_quantity_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_image',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_image', to='products.item'),
        ),
    ]
