from typing import Optional, Any, Dict
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.db.models import Sum, QuerySet
from django.contrib import messages
import json

from .models import Order


class OrderListView(ListView):
    """ Представляет список заказов с возможностью фильтрации по номеру стола и статусу. """
    
    model = Order
    template_name = "orders/order_list.html"
    context_object_name = "orders"

    def get_queryset(self) -> QuerySet[Order]:
        """
        Получает список заказов с учетом фильтрации.

        Возвращает:
            QuerySet[Order]: Отфильтрованный список заказов.
        """
        queryset: QuerySet[Order] = Order.objects.all()

        table_number: Optional[str] = self.request.GET.get("table_number")
        status: Optional[str] = self.request.GET.get("status")

        if table_number:
            queryset = queryset.filter(table_number=table_number)

        if status:
            queryset = queryset.filter(status=status)

        return queryset


class OrderCreateView(CreateView):
    """ Создает новый заказ. """

    model = Order
    fields = ["table_number", "status"]
    template_name = "orders/order_form.html"
    success_url = reverse_lazy("order_list")

    def form_valid(self, form: Any) -> HttpResponse:
        """
        Проверяет данные формы перед сохранением.

        Аргументы:
            form (Any): Форма с введенными данными.

        Возвращает:
            HttpResponse: Перенаправление в случае успеха или возврат ошибки.
        """
        items_json: Optional[str] = self.request.POST.get("items_json")
        
        if items_json:
            form.instance.items = json.loads(items_json)
        else:
            messages.error(self.request, "Ошибка: нельзя создать заказ без блюд!")
            return self.form_invalid(form)
        
        return super().form_valid(form)


class OrderUpdateView(UpdateView):
    """ Редактирует существующий заказ. """

    model = Order
    fields = ["table_number", "status"]
    template_name = "orders/order_form.html"
    success_url = "/orders/"

    def form_valid(self, form: Any) -> HttpResponse:
        """
        Проверяет данные формы перед обновлением заказа.

        Аргументы:
            form (Any): Форма с обновленными данными.

        Возвращает:
            HttpResponse: Перенаправление после успешного редактирования.
        """
        items_json: Optional[str] = self.request.POST.get("items_json")
        if items_json:
            form.instance.items = json.loads(items_json)
        return super().form_valid(form)


class OrderDeleteView(View):
    """ Удаляет заказ по его ID. """

    def post(self, request: HttpRequest, pk: int) -> HttpResponseRedirect:
        """
        Обрабатывает POST-запрос на удаление заказа.

        Аргументы:
            request (HttpRequest): Запрос пользователя.
            pk (int): Идентификатор удаляемого заказа.

        Возвращает:
            HttpResponseRedirect: Перенаправление на список заказов.
        """
        order: Order = get_object_or_404(Order, pk=pk)
        order.delete()
        return redirect(reverse("order_list"))


def revenue_view(request: HttpRequest) -> JsonResponse:
    """
    Рассчитывает общую выручку по всем оплаченным заказам.

    Аргументы:
        request (HttpRequest): Запрос пользователя.

    Возвращает:
        JsonResponse: JSON-ответ с суммой выручки.
    """
    total_revenue: Optional[float] = Order.objects.filter(status="paid").aggregate(Sum("total_price"))["total_price__sum"] or 0
    return JsonResponse({"total_revenue": total_revenue})
