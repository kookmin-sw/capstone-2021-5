# Generated by Django 3.1.6 on 2021-05-03 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0013_auto_20210502_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='default.jpg', null=True, upload_to=''),
        ),
    ]