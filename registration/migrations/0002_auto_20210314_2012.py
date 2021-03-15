# Generated by Django 3.1.6 on 2021-03-15 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '__first__'),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='event_title',
        ),
        migrations.AddField(
            model_name='registration',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registration_items', to='event.event'),
        ),
    ]
