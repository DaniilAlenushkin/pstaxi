# Generated by Django 3.2.5 on 2021-08-03 21:01

from django.db import migrations, models
import motorpool.models


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0009_auto_20210803_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=motorpool.models.get_upload_to_auto),
        ),
    ]