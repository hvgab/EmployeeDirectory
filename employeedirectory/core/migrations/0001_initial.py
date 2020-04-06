# Generated by Django 3.0.4 on 2020-03-27 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('phone', models.CharField(max_length=50, verbose_name='phone')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_number', models.IntegerField(verbose_name='employee-number')),
                ('firstname', models.CharField(max_length=50, verbose_name='firstname')),
                ('lastname', models.CharField(max_length=50, verbose_name='lastname')),
                ('phone', models.CharField(max_length=50, verbose_name='phone')),
                ('email', models.EmailField(max_length=320, unique=True, verbose_name='email')),
                ('address_street', models.CharField(max_length=50, verbose_name='street')),
                ('address_postcode', models.IntegerField(verbose_name='postcode')),
                ('address_city', models.CharField(max_length=50, verbose_name='city')),
                ('birthdate', models.DateField(verbose_name='birthdate')),
                ('ssn', models.IntegerField(verbose_name='social security number')),
                ('bank_account_number', models.CharField(max_length=50, verbose_name='bank account number')),
                ('is_employed', models.BooleanField(default=True, editable=False, help_text='Is the employee employed at the moment?')),
                ('emergency_contacts', models.ManyToManyField(to='core.EmergencyContact', verbose_name='emergency contacts')),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('start_date', models.DateField(auto_now_add=True, verbose_name='start_date')),
                ('end_date', models.DateField(verbose_name='end_date')),
            ],
        ),
        migrations.CreateModel(
            name='ExternalSystem',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('url', models.URLField(verbose_name='url')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExternalUserAccount',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=320)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Employee', verbose_name='')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ExternalSystem', verbose_name='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
