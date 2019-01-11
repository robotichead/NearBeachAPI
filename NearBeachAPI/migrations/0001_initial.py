# Generated by Django 2.1.5 on 2019-01-10 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='api_allowed_host',
            fields=[
                ('api_allowed_host_id', models.AutoField(primary_key=True, serialize=False)),
                ('allowed_host', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=5)),
            ],
            options={
                'db_table': 'api_allowed_host',
            },
        ),
        migrations.CreateModel(
            name='api_uuid',
            fields=[
                ('api_uuid_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=5)),
                ('change_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='api_uuid_change_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'api_uuid',
            },
        ),
        migrations.AddField(
            model_name='api_allowed_host',
            name='api_uuid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NearBeachAPI.api_uuid'),
        ),
        migrations.AddField(
            model_name='api_allowed_host',
            name='change_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='api_allowed_host_change_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
