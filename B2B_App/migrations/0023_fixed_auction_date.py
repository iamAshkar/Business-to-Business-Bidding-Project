# Generated by Django 4.0.3 on 2022-10-22 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('B2B_App', '0022_fixed_auction'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixed_auction',
            name='date',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
