from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),  # Панель администратора
    path('orders/', include('orders.urls')),  # Подключаем маршруты из приложения orders
    path('', RedirectView.as_view(pattern_name='order_list', permanent=True)),  # Редирект с / на /orders/
]