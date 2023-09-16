# Generated by Django 4.0.3 on 2022-10-21 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('B2B_App', '0018_rename_farmer_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='farmer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='B2B_App.farmer_reg'),
        ),
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
