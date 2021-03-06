# Generated by Django 3.0.3 on 2020-03-02 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=350, unique=True)),
                ('price', models.CharField(db_index=True, max_length=30)),
                ('url', models.CharField(db_index=True, max_length=350, unique=True)),
                ('description', models.TextField(db_index=True, max_length=5000)),
                ('category', models.CharField(db_index=True, max_length=100)),
                ('rating_reviews', models.CharField(db_index=True, default='without rating', max_length=100)),
                ('in_stock', models.BooleanField(default=True)),
                ('brand', models.CharField(db_index=True, default='without brand', max_length=100)),
                ('amount', models.CharField(db_index=True, default='quantity not indicated', max_length=10)),
                ('delivery_price', models.CharField(db_index=True, default='Free delivery', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', verbose_name='id_products')),
            ],
        ),
    ]
