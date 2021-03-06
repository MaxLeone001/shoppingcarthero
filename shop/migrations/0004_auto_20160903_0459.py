# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 04:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_item_item_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='item_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='item_quantity',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_id',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_image',
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='/Users/maxleone/repos/shoppingcarthero/shoppingcarthero/staticimg/no_image.png', upload_to='/Users/maxleone/repos/shoppingcarthero/shoppingcarthero/media/img/'),
        ),
    ]
