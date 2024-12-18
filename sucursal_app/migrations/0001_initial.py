# Generated by Django 5.1.3 on 2024-12-04 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id_sucursal', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nombre_sucursal', models.CharField(max_length=255)),
                ('numero_empleado', models.PositiveIntegerField()),
                ('calle_sucursal', models.CharField(max_length=255)),
                ('productos', models.CharField(max_length=255)),
                ('num_producto', models.PositiveIntegerField()),
                ('telefono', models.PositiveIntegerField()),
            ],
        ),
    ]
