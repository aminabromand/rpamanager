# Generated by Django 2.1 on 2018-08-21 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0006_auto_20180820_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicetask',
            name='application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.Application'),
        ),
    ]