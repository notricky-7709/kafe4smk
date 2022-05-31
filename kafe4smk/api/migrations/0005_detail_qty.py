# Generated by Django 3.2.7 on 2022-02-25 18:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_transaction_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='qty',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(1)]),
        ),
    ]
