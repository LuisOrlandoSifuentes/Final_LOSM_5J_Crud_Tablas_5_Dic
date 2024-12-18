# Generated by Django 5.1.3 on 2024-12-04 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('telefono', models.PositiveIntegerField()),
                ('producto', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('nie', models.CharField(max_length=50)),
                ('suc_asignadas', models.CharField(max_length=255)),
            ],
        ),
    ]
