# Generated by Django 4.0.3 on 2022-10-21 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('B2B_App', '0017_remove_product_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='farmer',
            new_name='user',
        ),
    ]
