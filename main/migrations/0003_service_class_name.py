# Generated by Django 4.2.6 on 2023-10-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_service_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='class_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
