# Generated by Django 5.0.6 on 2024-07-27 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_appointment_diagnosis_alter_appointment_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 27, 11, 40, 4, 19751, tzinfo=datetime.timezone.utc)),
        ),
    ]
