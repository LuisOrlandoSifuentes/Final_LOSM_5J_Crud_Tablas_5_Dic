# Generated by Django 5.1 on 2024-12-04 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.PositiveIntegerField()),
                ('tipo_de_pago', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
                ('productos_adquiridos', models.CharField(max_length=200)),
            ],
        ),
    ]
