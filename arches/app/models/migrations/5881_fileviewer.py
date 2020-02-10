# Generated by Django 2.2.8 on 2020-01-31 15:31

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("models", "5605_searchexporthistory_downloadfile"),
    ]

    operations = [
        migrations.RunSQL(
            """
            insert into card_components (componentid, name, description, component, componentname, defaultconfig) 
            values ('47e10bbb-cf09-4357-ace5-f824ac3bfd97', 'File Viewer', '', 'views/components/cards/file-viewer', 'file-viewer', '{}')
            """,
            """
            delete from card_components where componentid = '47e10bbb-cf09-4357-ace5-f824ac3bfd97';
            """,
        )
    ]
