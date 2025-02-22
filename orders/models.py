from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    ]

    table_number = models.PositiveIntegerField()
    items = models.JSONField()  # Список блюд с ценами
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def save(self, *args, **kwargs):
        self.total_price = sum(item.get('price', 0) for item in self.items) if self.items else 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Заказ {self.id} - Стол {self.table_number}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
