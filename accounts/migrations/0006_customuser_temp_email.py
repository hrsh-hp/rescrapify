# Generated by Django 5.0.2 on 2024-02-27 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customuser_phone_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='temp_email',
            field=models.EmailField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
