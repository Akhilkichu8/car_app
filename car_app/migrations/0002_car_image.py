# Generated by Django 3.2.3 on 2021-05-15 13:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='uploads/products/'),
            preserve_default=False,
        ),
    ]
