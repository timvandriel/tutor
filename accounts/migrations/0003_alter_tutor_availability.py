# Generated by Django 5.0.9 on 2024-10-16 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_tutor_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='availability',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
