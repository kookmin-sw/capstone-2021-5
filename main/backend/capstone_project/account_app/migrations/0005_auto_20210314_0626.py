# Generated by Django 3.1.6 on 2021-03-14 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0004_remove_customuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
