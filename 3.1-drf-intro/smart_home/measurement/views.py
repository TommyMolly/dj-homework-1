from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer

class SensorListCreateView(ListCreateAPIView):
    """
    Представление для создания нового датчика и получения списка всех датчиков.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SensorDetailSerializer
        return SensorSerializer


class SensorRetrieveUpdateView(RetrieveUpdateAPIView):
    """
    Представление для просмотра деталей и обновления существующего датчика.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreateView(CreateAPIView):
    """
    Представление для создания нового измерения температуры.
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer