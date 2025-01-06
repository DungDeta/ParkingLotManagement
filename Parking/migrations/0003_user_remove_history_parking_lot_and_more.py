# Generated by Django 5.1.3 on 2024-12-31 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0002_alter_history_options_alter_vehicle_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_rf_id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='RFID')),
                ('user_name', models.CharField(max_length=20, verbose_name='Tên')),
                ('vehicle_fee', models.FloatField(default=3000, verbose_name='Phí đỗ')),
                ('user_contact', models.CharField(max_length=20, verbose_name='Số điện thoại')),
            ],
            options={
                'verbose_name': 'Người dùng',
                'verbose_name_plural': 'Người dùng',
            },
        ),
        migrations.RemoveField(
            model_name='history',
            name='parking_lot',
        ),
        migrations.RemoveField(
            model_name='history',
            name='parking_slot',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='vehicle_fee',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='vehicle_owner_id',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_image',
            field=models.ImageField(blank=True, upload_to='Vehicle/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Parking.user', verbose_name='Chủ xe'),
        ),
    ]