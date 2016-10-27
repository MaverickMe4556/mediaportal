# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0006_album_event_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PressRelease',
        ),
    ]
