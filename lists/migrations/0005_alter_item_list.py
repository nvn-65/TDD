# Generated by Django 3.2.9 on 2021-11-27 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_item_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='lists.list'),
        ),
    ]
