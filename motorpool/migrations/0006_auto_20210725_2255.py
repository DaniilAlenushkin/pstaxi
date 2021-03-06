# Generated by Django 3.2.5 on 2021-07-25 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0005_auto_20210725_2234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='option',
            options={'verbose_name_plural': 'Опции'},
        ),
        migrations.CreateModel(
            name='VehiclePassport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(max_length=30, verbose_name='Идентификационный номер (VIN)')),
                ('engine_volume', models.PositiveSmallIntegerField(verbose_name='Объем двигателя, куб.см')),
                ('engine_power', models.PositiveSmallIntegerField(verbose_name='Мощность двигателя, л.с.')),
                ('auto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='motorpool.auto')),
            ],
            options={
                'verbose_name': 'Паспорт машины',
                'verbose_name_plural': 'Паспорта машин',
            },
        ),
    ]
