# Generated by Django 3.1.1 on 2020-10-09 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='AuthorModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=150)),
                ('description', models.CharField(default=None, max_length=1500, null=True)),
                ('birth_day', models.DateField(default=None, null=True)),
                ('country', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='author.countrymodel')),
            ],
            options={
                'db_table': 'author',
            },
        ),
    ]
