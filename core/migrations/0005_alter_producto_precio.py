# Generated by Django 4.0.5 on 2022-07-08 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_id_producto_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.BigIntegerField(null=True),
        ),
    ]
