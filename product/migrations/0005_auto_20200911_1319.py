# Generated by Django 2.0.3 on 2020-09-11 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200908_1641'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name_plural': 'images'},
        ),
    ]
