# Generated by Django 4.2.4 on 2023-08-16 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_rename_privacy_room_private'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='private',
            field=models.BooleanField(default=True),
        ),
    ]
