# Generated by Django 4.0.3 on 2022-10-21 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('B2B_App', '0015_auction_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
        migrations.AlterField(
            model_name='product',
            name='farmer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='B2B_App.farmer_reg'),
        ),
    ]