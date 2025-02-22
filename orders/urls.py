from django.urls import path
from .views import OrderListView, OrderCreateView, OrderUpdateView, OrderDeleteView, revenue_view

urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),  # Главная страница заказов
    path('add/', OrderCreateView.as_view(), name='order_add'),  # Добавление заказа
    path('edit/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),  # Редактирование заказа
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),  # Удаление заказа
    path("revenue/", revenue_view, name="order_revenue") # Страница с выручкой
]
