# Generated by Django 3.1.3 on 2021-04-27 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientpage', '0003_auto_20210427_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listviewpdf',
            name='link',
        ),
    ]