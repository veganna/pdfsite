# Generated by Django 3.1.3 on 2021-04-28 19:46

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientpage', '0010_auto_20210428_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listviewpdf',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True),
        ),
    ]
