# Generated by Django 4.2.7 on 2023-12-06 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_factura_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factura',
            old_name='producto',
            new_name='productos',
        ),
    ]
