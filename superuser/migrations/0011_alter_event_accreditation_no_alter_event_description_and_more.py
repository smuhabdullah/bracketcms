# Generated by Django 4.2 on 2023-05-09 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0010_event_accreditation_no_event_facility_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='accreditation_no',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='facility_number',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
