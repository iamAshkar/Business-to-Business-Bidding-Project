# Generated by Django 4.0.3 on 2022-10-22 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('B2B_App', '0020_delete_categ'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]
