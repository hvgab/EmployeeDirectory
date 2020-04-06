# Generated by Django 3.0.4 on 2020-04-05 19:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200405_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencycontact',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4e204857-75ee-4650-9d8f-1a024155dc60'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4e204857-75ee-4650-9d8f-1a024155dc60'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='employment',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4e204857-75ee-4650-9d8f-1a024155dc60'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='externalsystem',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4e204857-75ee-4650-9d8f-1a024155dc60'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='externaluseraccount',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4e204857-75ee-4650-9d8f-1a024155dc60'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
