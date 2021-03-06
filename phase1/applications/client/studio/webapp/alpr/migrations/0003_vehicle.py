# Generated by Django 4.0.5 on 2022-06-24 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpr', '0002_remove_document_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_number', models.CharField(max_length=30)),
                ('confidence', models.FloatField()),
                ('frame_no', models.IntegerField()),
                ('detected_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
