# Generated by Django 5.1.6 on 2025-02-22 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_category_image_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
