# Generated by Django 4.0.3 on 2022-06-06 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0008_alter_vehicle_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='options',
            field=models.ManyToManyField(related_name='vehicle', to='vehicle.option'),
        ),
    ]
