# Generated by Django 4.1.1 on 2023-03-30 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('B2B_App', '0030_auction_admin_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixed_auction',
            name='payment',
            field=models.CharField(max_length=100, null=True),
        ),
    ]