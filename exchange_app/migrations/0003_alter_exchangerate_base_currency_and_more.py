# Generated by Django 5.1.3 on 2024-11-14 18:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exchange_app", "0002_alter_exchangerate_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exchangerate",
            name="base_currency",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="base_rate",
                to="exchange_app.currency",
            ),
        ),
        migrations.AlterField(
            model_name="exchangerate",
            name="target_currency",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="target_rate",
                to="exchange_app.currency",
            ),
        ),
    ]
