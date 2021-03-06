# Generated by Django 3.0.4 on 2020-04-05 20:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200405_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencycontact',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b2eb8498-bab1-4838-9c18-94ae690bf4c7'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b2eb8498-bab1-4838-9c18-94ae690bf4c7'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='employment',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b2eb8498-bab1-4838-9c18-94ae690bf4c7'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='externalsystem',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b2eb8498-bab1-4838-9c18-94ae690bf4c7'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='externalsystem',
            name='slug',
            field=models.SlugField(max_length=15, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='externaluseraccount',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b2eb8498-bab1-4838-9c18-94ae690bf4c7'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
