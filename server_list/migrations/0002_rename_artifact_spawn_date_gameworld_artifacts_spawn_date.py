# Generated by Django 4.2.3 on 2024-03-10 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gameworld',
            old_name='artifact_spawn_date',
            new_name='artifacts_spawn_date',
        ),
    ]