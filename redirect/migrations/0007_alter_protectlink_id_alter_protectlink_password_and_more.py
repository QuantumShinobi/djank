# Generated by Django 5.1 on 2024-09-01 15:40

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redirect', '0006_protectlink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protectlink',
            name='id',
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='protectlink',
            name='password',
            field=models.UUIDField(default=uuid.UUID(
                '4c3a396f-3f6c-4075-a20c-cd8a3843b5a6'), editable=False),
        ),
        migrations.AlterField(
            model_name='redirect',
            name='id',
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='redirectlink',
            name='id',
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
