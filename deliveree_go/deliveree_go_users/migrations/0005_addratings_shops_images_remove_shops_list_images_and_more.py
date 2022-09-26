# Generated by Django 4.1.1 on 2022-09-19 17:31

import deliveree_go_users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveree_go_users', '0004_category_types_items_list_order_details_shops_list_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='addratings',
            fields=[
                ('rating_id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.CharField(max_length=200)),
                ('user_id', models.IntegerField()),
                ('item_id', models.IntegerField()),
                ('shop_id', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('created_on', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='shops_images',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('shop_id', models.IntegerField()),
                ('image', models.FileField(upload_to=deliveree_go_users.models.shopImage_directory_path)),
                ('created_on', models.CharField(default='', max_length=300)),
            ],
            options={
                'db_table': 'shops_images',
            },
        ),
        migrations.RemoveField(
            model_name='shops_list',
            name='images',
        ),
        migrations.AddField(
            model_name='category_types',
            name='image',
            field=models.FileField(default='', upload_to=deliveree_go_users.models.categoryImage_directory_path),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category_types',
            name='category_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='uid',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
    ]