# Generated by Django 5.0.2 on 2024-03-02 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_item_image_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='products.category'),
        ),
    ]
