# Generated by Django 3.2 on 2022-09-28 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_alter_song_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date_released',
            field=models.DateField(blank=True, null=True),
        ),
    ]
