# Generated by Django 5.0.2 on 2024-02-26 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_city_customuser_phone_no_customuser_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_no',
            field=models.IntegerField(blank=True, default=None, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='state',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
