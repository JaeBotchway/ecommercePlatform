# Generated by Django 4.0.3 on 2022-03-23 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('ELT', 'Electronics'), ('JGP', 'Jewellery'), ('MSC', 'Mens Clothing'), ('WSC', 'Womens Clothing'), ('FWS', 'Footwear')], max_length=10),
        ),
    ]