# Generated by Django 3.1.6 on 2021-03-13 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0003_auto_20210313_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='gender',
        ),
    ]
