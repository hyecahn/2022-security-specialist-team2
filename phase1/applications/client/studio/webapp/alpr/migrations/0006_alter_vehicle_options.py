# Generated by Django 4.0.5 on 2022-06-26 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alpr', '0005_alter_vehicle_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={'ordering': ['frame_no']},
        ),
    ]
