from django.contrib import admin
from .models import User, Vehicle, History

class VehicleInline(admin.TabularInline):  # Dùng TabularInline để hiển thị dạng bảng
    model = Vehicle
    extra = 0  # Không hiển thị thêm dòng trống để thêm phương tiện mới
    fields = ['vehicle_plates', 'vehicle_type', 'vehicle_company', 'vehicle_model', 'vehicle_color']  # Các trường hiển thị
    readonly_fields = ['vehicle_plates', 'vehicle_type', 'vehicle_company', 'vehicle_model', 'vehicle_color']  # Chỉ đọc

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_rf_id', 'user_contact', 'vehicle_fee', 'vehicle_count']
    search_fields = ['user_name', 'user_rf_id']
    inlines = [VehicleInline]

    def vehicle_count(self, obj):
        return obj.vehicle_set.count()  # Đếm số lượng phương tiện của User
    vehicle_count.short_description = "Số lượng phương tiện"  # Tiêu đề cột

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['vehicle_plates', 'vehicle_type', 'vehicle_owner', 'vehicle_company', 'vehicle_model']  # Hiển thị danh sách
    search_fields = ['vehicle_plates', 'vehicle_company', 'vehicle_owner__user_name']  # Cho phép tìm kiếm theo chủ xe

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'entry_time', 'exit_time', 'parking_charge']  # Các trường hiển thị trong danh sách History
    search_fields = ['vehicle__vehicle_plates']  # Tìm kiếm theo biển số xe
