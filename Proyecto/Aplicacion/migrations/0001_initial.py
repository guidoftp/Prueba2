# Generated by Django 3.2 on 2024-10-24 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=150)),
                ('fecha_lanz', models.DateField()),
                ('desarrolladora', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
            ],
        ),
    ]
