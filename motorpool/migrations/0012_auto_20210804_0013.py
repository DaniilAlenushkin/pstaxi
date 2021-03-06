# Generated by Django 3.2.5 on 2021-08-03 21:13

from django.db import migrations, models
import motorpool.models


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0011_auto_20210804_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=motorpool.models.get_upload_to_auto),
        ),
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='motorpool/brands/'),
        ),
    ]
