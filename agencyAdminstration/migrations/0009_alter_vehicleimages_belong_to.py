# Generated by Django 4.0.3 on 2022-04-04 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agencyAdminstration', '0008_vehicletype_remove_vehicle_vehicle_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleimages',
            name='belong_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='agencyAdminstration.vehicle'),
        ),
    ]
