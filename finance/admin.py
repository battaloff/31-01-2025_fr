from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Client, Expense, Income, AuditLog


@admin.register(Client)
class ClientAdmin(ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone', 'email')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Expense)
class ExpenseAdmin(ModelAdmin):
    list_display = ('category', 'amount',  'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('category', 'description')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Income)
class IncomeAdmin(ModelAdmin):
    list_display = ('client', 'process', 'sheets', 'amount', 'total_price', 'created_at')
    list_filter = ('process', 'created_at')
    search_fields = ('client__name', 'process', 'description')
    readonly_fields = ('created_at', 'updated_at')



@admin.register(AuditLog)
class AuditLogAdmin(ModelAdmin):
    list_display = ('user', 'action', 'model_name', 'record_id', 'created_at')
    list_filter = ('user', 'action', 'model_name', 'created_at')
    search_fields = ('user__username', 'model_name', 'details')
    readonly_fields = ('created_at',)
