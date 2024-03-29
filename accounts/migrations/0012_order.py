# Generated by Django 5.0.2 on 2024-03-18 13:25

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_rename_recipe_likedproducts_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.IntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MaxValueValidator(999999999999), django.core.validators.MinValueValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.CharField(blank=True, max_length=150, null=True)),
                ('state', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_cart', to='accounts.cart')),
            ],
        ),
    ]
