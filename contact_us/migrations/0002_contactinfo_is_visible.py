# Generated by Django 5.1 on 2024-08-15 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]
