# Generated by Django 2.1 on 2018-08-16 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calcschemas', '0001_initial'),
        ('processes', '0003_servicetask_gateway_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetask',
            name='calcschema',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='calcschemas.CalcSchema'),
        ),
    ]
