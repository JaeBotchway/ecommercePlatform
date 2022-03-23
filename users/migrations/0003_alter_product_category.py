# Generated by Django 4.0.3 on 2022-03-23 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_product_category_alter_product_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('ELT', 'Electronics'), ('JGP', 'Jewellery'), ('MSC', 'Mens Clothing'), ('WSC', 'Womens Clothing'), ('FWS', 'Footwear')], max_length=10),
        ),
    ]
