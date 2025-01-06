from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Vehicle, History, User
from .serializers import HistorySerializer, VehicleSerializer


class CheckRFIDAPI(APIView):
    def post(self, request):
        # Lấy dữ liệu từ request
        vehicle_plate = request.data.get("vehicle_plate")
        user_rf_id = request.data.get("user_rf_id")

        if not vehicle_plate or not user_rf_id:
            return Response(
                {"error": "Thiếu thông tin về biển số xe hoặc thẻ RFID."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Tìm kiếm người dùng và phương tiện trong database
        user = User.objects.filter(user_rf_id=user_rf_id).first()
        if not user:
            return Response(
                {"error": "Không tìm thấy người dùng với RFID đã cung cấp."},
                status=status.HTTP_404_NOT_FOUND,
            )

        vehicle = Vehicle.objects.filter(vehicle_plates=vehicle_plate, vehicle_owner=user).first()
        if not vehicle:
            return Response(
                {"error": "Không tìm thấy phương tiện hoặc phương tiện không thuộc sở hữu của người dùng."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Kiểm tra xem xe đã ở trong bến chưa
        in_parking = History.objects.filter(vehicle=vehicle, exit_time__isnull=True).exists()
        if in_parking:
            return Response(
                {"error": "Xe hiện đang ở trong bến."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = VehicleSerializer(vehicle)
        return Response(
            {"message": "Thông tin chính xác", "vehicle_info": serializer.data},
            status=status.HTTP_200_OK,
        )


class ParkingLogAPI(APIView):
    def post(self, request):
        # Lấy dữ liệu từ request
        vehicle_plate = request.data.get("vehicle_plate")
        user_rf_id = request.data.get("user_rf_id")
        parking_charge = request.data.get("parking_charge")
        image = request.FILES.get("image")

        if not vehicle_plate or not user_rf_id:
            return Response(
                {"error": "Thiếu thông tin về biển số xe hoặc thẻ RFID."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Xác nhận người dùng và phương tiện
        user = User.objects.filter(user_rf_id=user_rf_id).first()
        if not user:
            return Response(
                {"error": "Không tìm thấy người dùng với RFID đã cung cấp."},
                status=status.HTTP_404_NOT_FOUND,
            )

        vehicle = Vehicle.objects.filter(vehicle_plates=vehicle_plate, vehicle_owner=user).first()
        if not vehicle:
            return Response(
                {"error": "Không tìm thấy phương tiện hoặc phương tiện không thuộc sở hữu của người dùng."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Ghi lịch sử vào model History
        history = History.objects.create(
            vehicle=vehicle,
            parking_charge=float(parking_charge) if parking_charge else 3000,
            image=image,
        )

        # Cập nhật tổng phí đỗ xe
        user.vehicle_fee += float(parking_charge) if parking_charge else 3000
        user.save()

        return Response(
            {
                "message": "Đã ghi nhận lịch sử đỗ xe.",
                "history": HistorySerializer(history).data,
            },
            status=status.HTTP_201_CREATED,
        )