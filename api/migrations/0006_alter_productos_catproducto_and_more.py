# Generated by Django 4.2.7 on 2023-12-05 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_factura_cliente_alter_productos_canproducto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='catProducto',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='productos',
            name='precioProducto',
            field=models.PositiveIntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='cantidad',
            field=models.CharField(max_length=20),
        ),
    ]
