# Generated by Django 4.1.3 on 2022-11-22 15:01

import deliveree_go_users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveree_go_users', '0003_cart_list_modified_on_cart_list_total_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='items_Images',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_id', models.IntegerField()),
                ('image', models.FileField(upload_to=deliveree_go_users.models.itemImage_directory_path)),
                ('created_on', models.CharField(default='', max_length=200)),
            ],
            options={
                'db_table': 'items_images',
            },
        ),
    ]
