from django.db import models
from django.db.models import Sum

# Create your models here.
class Vehicle(models.Model):
    vehicle_plates = models.CharField(max_length=20, verbose_name="Biển số xe", primary_key=True, default='00A-0000')
    vehicle_type = models.CharField(max_length=20, verbose_name="Loại xe")
    vehicle_image = models.ImageField(
        upload_to='Vehicle/%Y/%m/%d',
        blank=True
    )
    vehicle_company = models.CharField(max_length=20, verbose_name="Hãng xe")
    vehicle_model = models.CharField(max_length=20,default='Unknown', verbose_name="Model")
    vehicle_color = models.CharField(max_length=20, default='Unknown', verbose_name="Màu sắc")
    vehicle_owner = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="Chủ xe")

    class Meta:
        verbose_name = "Xe"
        verbose_name_plural = "Xe"

    def __str__(self):
        return self.vehicle_plates



class User(models.Model):
    user_rf_id = models.CharField(max_length=20, verbose_name="RFID", primary_key=True)
    user_name = models.CharField(max_length=20, verbose_name="Tên")
    vehicle_fee= models.FloatField(default=3000, verbose_name="Phí đỗ")
    user_contact = models.CharField(max_length=20, verbose_name="Số điện thoại")

    class Meta:
        verbose_name = "Người dùng"
        verbose_name_plural = "Người dùng"

    def __str__(self):
        return self.user_name


class History(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    entry_time = models.DateTimeField(null=True, blank=True, auto_now_add=True, verbose_name="Thời gian vào")
    exit_time = models.DateTimeField(null=True, blank=True, verbose_name="Thời gian ra")
    parking_charge = models.FloatField(default=3000, verbose_name="Phí đỗ")
    image = models.ImageField(
        upload_to='History/%Y/%m/%d',
        blank=True
    )

    class Meta:
        verbose_name = "Lịch sử"
        verbose_name_plural = "Lịch sử"
        ordering = ['-entry_time']

    def __str__(self):
        return self.vehicle.vehicle_plates
