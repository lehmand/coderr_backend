# Generated by Django 5.1.6 on 2025-03-06 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
