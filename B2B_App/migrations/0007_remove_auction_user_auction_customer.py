# Generated by Django 4.1.1 on 2022-10-10 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('B2B_App', '0006_auction_status_alter_product_auction_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='user',
        ),
        migrations.AddField(
            model_name='auction',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='B2B_App.customer_reg'),
        ),
    ]