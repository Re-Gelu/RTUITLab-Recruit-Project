# Generated by Django 4.2.1 on 2023-05-13 15:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0016_events_is_avaliable_paidevents_is_avaliable_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="events",
            name="is_avaliable",
        ),
        migrations.RemoveField(
            model_name="paidevents",
            name="is_avaliable",
        ),
        migrations.RemoveField(
            model_name="privateevents",
            name="is_avaliable",
        ),
    ]
