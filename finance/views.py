from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Client, Expense, Income, AuditLog
from .forms import ClientForm, ExpenseForm, IncomeForm


# Главная страница (Dashboard)
@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user)
    incomes = Income.objects.filter(user=request.user)
    return render(request, 'finance/dashboard.html', {'expenses': expenses, 'incomes': incomes})


# Добавление клиента
@login_required
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.user = request.user
            client.save()
            return redirect('dashboard')
    else:
        form = ClientForm()
    return render(request, 'finance/add_client.html', {'form': form})


# Добавление расхода
@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()
    return render(request, 'finance/add_expense.html', {'form': form})


# Добавление дохода
@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST, request.FILES)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('dashboard')
    else:
        form = IncomeForm()
        form.fields['client'].queryset = Client.objects.filter(
            user=request.user)  # Фильтруем клиентов по текущему пользователю
    return render(request, 'finance/add_income.html', {'form': form})


# Детализация (фильтрация и сортировка)
@login_required
def detail_view(request):
    expenses = Expense.objects.filter(user=request.user)
    incomes = Income.objects.filter(user=request.user)
    return render(request, 'finance/detail.html', {'expenses': expenses, 'incomes': incomes})


# Удаление записи
@login_required
def delete_record(request, model_name, record_id):
    if model_name == 'expense':
        record = get_object_or_404(Expense, id=record_id, user=request.user)
    elif model_name == 'income':
        record = get_object_or_404(Income, id=record_id, user=request.user)
    elif model_name == 'client':
        record = get_object_or_404(Client, id=record_id, user=request.user)
    else:
        return redirect('dashboard')

    record.delete()
    return redirect('dashboard')
