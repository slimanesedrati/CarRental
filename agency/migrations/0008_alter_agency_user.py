# Generated by Django 4.0.3 on 2022-04-22 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agency', '0007_agency_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='agency', to=settings.AUTH_USER_MODEL),
        ),
    ]
