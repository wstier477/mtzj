# Generated by Django 5.1.7 on 2025-04-17 12:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "status_management",
            "0002_alter_status_options_alter_status_concentrate_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="status",
            name="created_at",
            field=models.DateField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="创建日期",
            ),
            preserve_default=False,
        ),
    ]
