# Generated by Django 5.0.2 on 2024-02-29 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customuser_temp_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='forgot_password_token',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
