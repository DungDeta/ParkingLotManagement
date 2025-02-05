# Generated by Django 5.1.3 on 2024-12-31 06:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Parking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='history',
            options={'ordering': ['-entry_time'], 'verbose_name': 'Lịch sử', 'verbose_name_plural': 'Lịch sử'},
        ),
        migrations.AlterModelOptions(
            name='vehicle',
            options={'verbose_name': 'Xe', 'verbose_name_plural': 'Xe'},
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='id',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='vehicle_number',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_fee',
            field=models.FloatField(default=3000, verbose_name='Phí đỗ'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_plates',
            field=models.CharField(default='00A-0000', max_length=20, primary_key=True, serialize=False,
                                   verbose_name='Biển số xe'),
        ),
        migrations.AlterField(
            model_name='history',
            name='entry_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Thời gian vào'),
        ),
        migrations.AlterField(
            model_name='history',
            name='exit_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Thời gian ra'),
        ),
        migrations.AlterField(
            model_name='history',
            name='image',
            field=models.ImageField(blank=True, upload_to='History/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='history',
            name='parking_charge',
            field=models.FloatField(default=3000, verbose_name='Phí đỗ'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_company',
            field=models.CharField(max_length=20, verbose_name='Hãng xe'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.CharField(max_length=20, verbose_name='Loại xe'),
        ),
    ]
