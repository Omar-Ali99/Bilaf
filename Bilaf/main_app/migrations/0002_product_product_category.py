# Generated by Django 4.2.2 on 2023-06-17 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.CharField(default='None', max_length=2048),
        ),
    ]