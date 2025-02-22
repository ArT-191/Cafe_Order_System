from .models import Order
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.db.models import Sum, Q
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
import json

class OrderListView(ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = Order.objects.all()
        
        table_number = self.request.GET.get('table_number')
        status = self.request.GET.get('status')

        if table_number:
            queryset = queryset.filter(table_number=table_number)

        if status:
            queryset = queryset.filter(status=status)

        return queryset

class OrderCreateView(CreateView):
    model = Order
    fields = ['table_number', 'status']
    template_name = 'orders/order_form.html'
    success_url = reverse_lazy('order_list')

    def form_valid(self, form):
        items_json = self.request.POST.get("items_json")  
        if items_json:
            form.instance.items = json.loads(items_json)
        else:
            messages.error(self.request, "Ошибка: нельзя создать заказ без блюд!")
            return self.form_invalid(form)
        return super().form_valid(form)

class OrderUpdateView(UpdateView):
    model = Order
    fields = ['table_number', 'status']
    template_name = 'orders/order_form.html'
    success_url = '/orders/'

    def form_valid(self, form):
        items_json = self.request.POST.get("items_json")
        if items_json:
            form.instance.items = json.loads(items_json)
        return super().form_valid(form)
    
class OrderDeleteView(View):
    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.delete()
        return redirect(reverse("order_list"))
    
def revenue_view(request):
    total_revenue = Order.objects.filter(status="paid").aggregate(Sum("total_price"))["total_price__sum"] or 0
    return JsonResponse({"total_revenue": total_revenue})

    def get_queryset(self):
        revenue = Order.objects.filter(status='paid').aggregate(total_revenue=Sum('total_price'))
        print(revenue)  
        return revenue
