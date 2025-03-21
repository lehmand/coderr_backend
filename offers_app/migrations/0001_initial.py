# Generated by Django 5.1.6 on 2025-03-19 18:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.FileField(blank=True, null=True, upload_to=None)),
                ('description', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('min_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('min_delivery_time', models.PositiveIntegerField(default=7)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OfferDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('revisions', models.PositiveIntegerField(default=0)),
                ('delivery_time_in_days', models.PositiveIntegerField(default=0)),
                ('price', models.PositiveIntegerField(default=100)),
                ('features', models.JSONField(default=list)),
                ('offer_type', models.CharField(max_length=200)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='offers_app.offer')),
            ],
        ),
    ]
