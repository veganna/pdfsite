# Generated by Django 3.1.3 on 2021-04-27 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_ifpaid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
    ]
