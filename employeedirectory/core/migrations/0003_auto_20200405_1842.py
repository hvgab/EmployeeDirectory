# Generated by Django 3.0.4 on 2020-04-05 16:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200404_1222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employment',
            old_name='title',
            new_name='jobtitle',
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e7e3af1d-fe0e-4343-9acf-f505b1fe8b04'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e7e3af1d-fe0e-4343-9acf-f505b1fe8b04'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='employment',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e7e3af1d-fe0e-4343-9acf-f505b1fe8b04'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='employment',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 5, 16, 42, 21, 591307, tzinfo=utc), verbose_name='start_date'),
        ),
        migrations.AlterField(
            model_name='externalsystem',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e7e3af1d-fe0e-4343-9acf-f505b1fe8b04'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='externaluseraccount',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e7e3af1d-fe0e-4343-9acf-f505b1fe8b04'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
