# Generated by Django 3.2.6 on 2023-09-02 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candle',
            old_name='close',
            new_name='CLOSE',
        ),
        migrations.RenameField(
            model_name='candle',
            old_name='date',
            new_name='DATE',
        ),
        migrations.RenameField(
            model_name='candle',
            old_name='high',
            new_name='HIGH',
        ),
        migrations.RenameField(
            model_name='candle',
            old_name='low',
            new_name='LOW',
        ),
        migrations.RenameField(
            model_name='candle',
            old_name='open',
            new_name='OPEN',
        ),
    ]
