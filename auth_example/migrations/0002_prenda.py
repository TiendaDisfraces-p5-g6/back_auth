# Generated by Django 3.2.9 on 2021-11-21 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_example', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prenda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_prenda', models.CharField(max_length=12)),
                ('descripcion', models.CharField(max_length=100)),
                ('talla', models.CharField(max_length=3)),
                ('cantidad', models.IntegerField(default=0)),
            ],
        ),
    ]
