# Sử dụng image Python
FROM python:3.12

# Đặt thư mục làm việc
WORKDIR /ParkingLotManagement

# Copy tất cả files vào container
COPY . /ParkingLotManagement/

# Cài đặt dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Chạy server Django (lệnh được khai báo trong docker-compose.yml)