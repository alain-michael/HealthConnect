# Generated by Django 5.0.6 on 2024-07-30 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_pastmetrics_updated_field_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastmetrics',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
