# Generated by Django 4.1.1 on 2022-09-12 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_currency', models.CharField(max_length=50, verbose_name='Название валюты')),
            ],
            options={
                'verbose_name': 'Валюта',
                'verbose_name_plural': 'Валюты',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название продукта')),
                ('description', models.CharField(max_length=300, verbose_name='Описание товара')),
                ('product_image', models.ImageField(upload_to='products_images/', verbose_name='Фотография продукта')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='categories.category', verbose_name='Категория товара')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_currency', to='products.currency', verbose_name='Название валюты')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_product', to=settings.AUTH_USER_MODEL, verbose_name='Владелец товара')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]