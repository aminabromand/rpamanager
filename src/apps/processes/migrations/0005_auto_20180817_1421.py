# Generated by Django 2.1 on 2018-08-17 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0004_servicetask_calcschema'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='app_tpye',
            new_name='app_type',
        ),
        migrations.RenameField(
            model_name='servicetask',
            old_name='schedule_tpye',
            new_name='schedule_type',
        ),
    ]
