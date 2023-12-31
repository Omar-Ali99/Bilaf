# Generated by Django 4.2.2 on 2023-06-17 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0008_remove_store_commercial_registration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='instagram_link',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='store',
            name='snapchat_link',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='store',
            name='twitter_link',
            field=models.URLField(blank=True, default=''),
        ),
    ]
