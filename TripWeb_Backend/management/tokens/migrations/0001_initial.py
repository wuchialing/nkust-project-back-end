# Generated by Django 5.2 on 2025-05-14 07:47

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("trip", "0009_delete_triptoken"),
    ]

    operations = [
        migrations.CreateModel(
            name="TripToken",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "token_amount",
                    models.IntegerField(help_text="此日期時段發行的第 x 顆代幣"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("UNISSUED", "尚未發行"),
                            ("ISSUED", "已發行"),
                            ("SOLD_OUT", "已售罄"),
                        ],
                        default="UNISSUED",
                        help_text="代幣的狀態，例：尚未發行、已發行、已售罄",
                        max_length=10,
                    ),
                ),
                (
                    "trip_schedule",
                    models.ForeignKey(
                        help_text="此代幣所屬的日期時段",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tokens",
                        to="trip.tripschedule",
                    ),
                ),
            ],
        ),
    ]
