# Generated by Django 4.0.3 on 2022-03-23 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('ELT', 'Electronics'), ('JGP', 'Jewellery'), ('MSC', 'Mens Clothing'), ('WSC', 'Womens Clothing'), ('FWS', 'Footwear')], default='FWS', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]