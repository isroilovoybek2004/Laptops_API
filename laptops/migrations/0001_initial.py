# Generated by Django 5.0.2 on 2024-03-01 10:51

import django.core.validators
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
            name='Laptops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('manufacturer', models.TextField()),
                ('description', models.TextField()),
                ('image_laptop', models.ImageField(default='laptops_images/default_laptop_image.jpg', upload_to='media/laptops_images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'laptops_table',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'manufacturer_table',
            },
        ),
        migrations.CreateModel(
            name='LaptopReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('star_given', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='laptops.laptops')),
            ],
            options={
                'db_table': 'review_table',
            },
        ),
    ]