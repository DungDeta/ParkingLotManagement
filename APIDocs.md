# API Documentation

## 1. CheckRFIDAPI: Kiểm Tra Thông Tin Phương Tiện và Người Dùng

### Endpoint: `/api/check_rfid/`
- **Method**: `POST`
- **Description**: Kiểm tra thông tin về phương tiện và người dùng dựa trên thẻ RFID và biển số xe.

### Request Body:
```json
{
  "vehicle_plate": "29A-12345",
  "user_rf_id": "RFID001"
}
```
### Parameters:
- `vehicle_plate`: Biển số xe
- `user_rf_id`: Mã RFID của người dùng

### Response:
- **Status Code**: 200
- **Content**:
```json
{
  "message": "Thông tin chính xác",
  "vehicle_info": {
    "vehicle_plates": "29A-12345",
    "vehicle_type": "Ô tô",
    "vehicle_company": "Toyota",
    "vehicle_model": "Corolla",
    "vehicle_color": "Đỏ",
    "vehicle_owner": "RFID001",
    "vehicle_owner_contact": "0123456789",
    "vehicle_owner_address": "Hà Nội",
    "vehicle_owner_email": "nguyenvana@example.com"
  }
}
```

## 2. ParkingLogAPI: Ghi Lịch Sử Đỗ Xe

### Endpoint: `/api/parking_log/
- **Method**: `POST`
- **Description**: Ghi lại thông tin về thời gian đỗ xe của phương tiện và tính phí đỗ xe.

### Request Body:
```json
{
  "vehicle_plate": "29A-12345",
  "user_rf_id": "RFID001",
  "parking_charge": 5000
}
```
### Parameters:
- `vehicle_plate`: Biển số xe
- `user_rf_id`: Mã RFID của người dùng
- `parking_charge`: Phí đỗ xe

### Response:
- **Status Code**: 200
- **Content**:
```json
{
  "message": "Đã ghi nhận lịch sử đỗ xe.",
  "history": {
    "vehicle": "29A-12345",
    "entry_time": "2024-12-31T08:00:00Z",
    "exit_time": "2024-12-31T10:00:00Z",
    "parking_charge": 5000,
    "image": "path/to/image.jpg"
  }
}

```