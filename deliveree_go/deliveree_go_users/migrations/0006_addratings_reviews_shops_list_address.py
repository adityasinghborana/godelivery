# Generated by Django 4.1.1 on 2022-09-20 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveree_go_users', '0005_addratings_shops_images_remove_shops_list_images_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addratings',
            name='reviews',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='shops_list',
            name='address',
            field=models.TextField(default=''),
        ),
    ]