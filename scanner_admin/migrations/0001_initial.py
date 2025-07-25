# Generated by Django 5.1.5 on 2025-04-04 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='scanner',
            fields=[
                ('scanner_id', models.AutoField(primary_key=True, serialize=False)),
                ('scanner_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'scanr_approval_persons',
                'managed': False,
            },
        ),
    ]
