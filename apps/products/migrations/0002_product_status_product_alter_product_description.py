# Generated by Django 4.1.1 on 2022-09-16 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status_product',
            field=models.BooleanField(default=False, verbose_name='Статус продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=500, verbose_name='Описание товара'),
        ),
    ]