# Generated by Django 3.1.3 on 2021-04-28 17:10

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientpage', '0008_auto_20210427_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='listviewpdf',
            name='total_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listviewpdf',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name'),
        ),
    ]
