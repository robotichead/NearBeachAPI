# Generated by Django 2.1.5 on 2019-01-10 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeachAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='api_uuid',
            name='api_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
