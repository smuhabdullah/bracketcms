# Generated by Django 4.2 on 2023-05-08 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0009_remove_answer_order_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='accreditation_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='facility_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='mumaris_days',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]