# Generated by Django 4.0.3 on 2022-10-22 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('B2B_App', '0023_fixed_auction_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixed_auction',
            name='farmer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='B2B_App.farmer_reg'),
        ),
    ]
