from django.shortcuts import render, redirect
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
def landing(request):

    return render(request, 'dashboard/landing.html')


@login_required
def dashboard(request):
    current_user = request.user
    expenses = Expenses.objects.filter(user=current_user).all()
    expenses.reverse()
    if request.method=='POST':
        form = IncomeForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid:
            form.save()
            return redirect('dashboard')
    else:
        form = IncomeForm(instance=request.user.profile)

    total_exp = Expenses.objects.filter(user=current_user).all()
    sumb = sum(total_exp.values_list('amount', flat=True))

    print(sumb)
    income = current_user.profile.income
    result = income - sumb
    context = {
        'form':form,
        'income':income,
        'sumb':sumb,
        'result':result,
        'total':total_exp,
        'expenses':expenses[::-1],
        'current_user':current_user
    }
    
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def expenses(request):
    current_user = request.user
    expenses = Expenses.objects.filter(user=current_user).all()
    expenses.reverse()
    
    
    if request.method == 'POST':
        form = NewExpenditureForm(request.POST)
        if form.is_valid():
            Expenses.user_id = request.user
            description = form.cleaned_data.get('Description')
            amount = form.cleaned_data.get('Amount')
            category = form.cleaned_data.get('Category')
            
            p, created = Expenses.objects.get_or_create(description=description, amount=amount, category=category, user=current_user)
            form.save(commit=False)
            return redirect('expenses')
    else:
        form = NewExpenditureForm()
        
    context = {
        'expenses':expenses[::-1],
        'current_user':current_user,
        'form':form,
    }
    
    return render(request, 'dashboard/expenses.html', context)


@login_required
def search(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewExpenditureForm(request.POST)
        if form.is_valid():
            Expenses.user_id = request.user
            description = form.cleaned_data.get('Description')
            amount = form.cleaned_data.get('Amount')
            category = form.cleaned_data.get('Category')
            
            p, created = Expenses.objects.get_or_create(description=description, amount=amount, category=category, user=current_user)
            form.save(commit=False)
            return redirect('expenses')
    else:
        form = NewExpenditureForm()
    if 'exp' in request.GET and request.GET["exp"]:
        search_term = request.GET.get("exp")
        searched_expenses = Expenses.search_by_description(search_term)
        message = f"{search_term}"

        return render(request, 'dashboard/search.html',{"message":message,"expenses": searched_expenses,'current_user':current_user,'form':form,})

    else:
        message = "You haven't searched for any term"
        return render(request, 'dashboard/search.html',{"message":message,'current_user':current_user,'form':form,})