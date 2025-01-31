from django.db import models
from django.contrib.auth.models import User



class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя клиента")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('lunch', 'Обед'),
        ('raw_materials', 'Сырьё'),
        ('rent', 'Аренда'),
        ('other', 'Другое'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Категория")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    photo = models.ImageField(upload_to='expenses/', null=True, blank=True, verbose_name="Фото")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f"{self.get_category_display()} - {self.amount}"

    class Meta:
        verbose_name = "Расход"
        verbose_name_plural = "Расходы"


from django.db import models
from django.contrib.auth.models import User

class Income(models.Model):
    PROCESS_CHOICES = [
        ('lacquering', 'Лакировка'),
        ('lamination', 'Ламинация'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    process = models.CharField(max_length=50, choices=PROCESS_CHOICES, verbose_name="Процесс")
    sheets = models.IntegerField(verbose_name="Количество листов")
    amount = models.DecimalField(max_digits=20, decimal_places=0, verbose_name="Цена за лист")
    photo = models.ImageField(upload_to='incomes/', null=True, blank=True, verbose_name="Фото")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def total_price(self):
        """Рассчитывает общую стоимость заказа."""
        return self.amount * self.sheets

    total_price.short_description = "Общая стоимость"

    def __str__(self):
        return f"{self.client.name} - {self.get_process_display()} - {self.total_price()}"

    class Meta:
        verbose_name = "Доход"
        verbose_name_plural = "Доходы"


class AuditLog(models.Model):
    ACTION_CHOICES = [
        ('create', 'Создание'),
        ('update', 'Обновление'),
        ('delete', 'Удаление'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    action = models.CharField(max_length=50, choices=ACTION_CHOICES, verbose_name="Действие")
    model_name = models.CharField(max_length=100, verbose_name="Модель")
    record_id = models.IntegerField(verbose_name="ID записи")
    details = models.TextField(verbose_name="Детали")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.model_name}"

    class Meta:
        verbose_name = "Лог аудита"
        verbose_name_plural = "Логи аудита"
