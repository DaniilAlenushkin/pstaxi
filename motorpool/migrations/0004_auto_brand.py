# Generated by Django 3.2.5 on 2021-07-25 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0003_auto_20210725_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='motorpool.brand'),
        ),
    ]
