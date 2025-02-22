from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

     # Добавляем поиск
    filter_backends = [filters.SearchFilter]
    search_fields = ['table_number', 'status'] 

    def create(self, request, *args, **kwargs):
        if not request.data.get('items'): 
            return Response({'error': 'Список блюд не может быть пустым!'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
