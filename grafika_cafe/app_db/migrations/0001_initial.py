# Generated by Django 4.0.4 on 2022-05-18 05:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('harga', models.IntegerField()),
            ],
            options={
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('level', models.CharField(choices=[('Kasir', 'Kasir'), ('Manager', 'Manager'), ('Admin', 'Admin')], default='Kasir', max_length=10)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('cashier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_db.user')),
            ],
            options={
                'db_table': 'transaksi',
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(1)])),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_db.menu')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_db.transaksi')),
            ],
            options={
                'db_table': 'list',
            },
        ),
        migrations.CreateModel(
            name='Aktivitas',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_db.user')),
            ],
            options={
                'db_table': 'aktivitas',
            },
        ),
    ]
