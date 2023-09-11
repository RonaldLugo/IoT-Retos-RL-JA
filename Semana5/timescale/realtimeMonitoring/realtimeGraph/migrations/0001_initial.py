# Generated by Django 3.2.4 on 2022-03-06 23:46

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import realtimeGraph.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('code', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200)),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('lng', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('active', models.BooleanField(default=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realtimeGraph.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realtimeGraph.country')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=50)),
                ('max_value', models.FloatField(blank=True, default=None, null=True)),
                ('min_value', models.FloatField(blank=True, default=None, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('login', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('password', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=60)),
                ('active', models.BooleanField(default=True)),
                ('role', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='realtimeGraph.role')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_activity', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('location', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='realtimeGraph.location')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='realtimeGraph.user')),
            ],
            options={
                'unique_together': {('user', 'location')},
            },
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realtimeGraph.state'),
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('time', models.BigIntegerField(default=realtimeGraph.models.Data.timestamp_now, primary_key=True, serialize=False)),
                ('base_time', models.DateTimeField(default=realtimeGraph.models.Data.base_time_now)),
                ('min_value', models.FloatField(blank=True, default=None, null=True)),
                ('max_value', models.FloatField(blank=True, default=None, null=True)),
                ('length', models.IntegerField(default=0)),
                ('avg_value', models.FloatField(blank=True, default=None, null=True)),
                ('times', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=list, size=None)),
                ('values', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=list, size=None)),
                ('measurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realtimeGraph.measurement')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realtimeGraph.station')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together={('city', 'state', 'country')},
        ),
        migrations.AddConstraint(
            model_name='data',
            constraint=models.UniqueConstraint(fields=('time', 'base_time', 'station_id', 'measurement_id'), name='unique data measure'),
        ),
    ]
