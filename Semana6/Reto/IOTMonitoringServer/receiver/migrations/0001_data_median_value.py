# Generated by Django 4.2.5 on 2023-09-15 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiver', 'to_timescale'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='median_value',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
