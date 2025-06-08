from django.shortcuts import render,redirect
from .models import*
from user_auth.models import*
from decimal import Decimal
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def dashboard(request):

    reg_user, _ = Reg_user.objects.get_or_create(user=request.user)
    dashboard, _ = Dashboard.objects.get_or_create(user=reg_user)
    transactions = Transaction.objects.filter(user=reg_user)
    

    css = 'dashboard.css'
    context = {'css':css,'dashboard':dashboard,'transactions':transactions}
    return render(request,'dashboard.html',context)

@login_required
def transactions(request):
    
        

    reg_user = Reg_user.objects.get(user = request.user)
    trans = Transaction.objects.filter(user=reg_user)
    css = 'transactions.css'
    context = {'css':css,'transactions':trans}
    return render(request,'transactions.html',context)

@login_required
def add_transaction(request):
    if request.method == 'POST':
        reg_user = Reg_user.objects.get(user=request.user)
        data = request.POST
        t_amount = Decimal(data.get('amount'))
        t_type = data.get('transaction_type')
        t_catagory = data.get('category')
       

        Transaction.objects.create(
            user = reg_user,
            amount = t_amount,
            catagory = t_catagory,
            transaction_type = t_type 
        )

        dashboard = Dashboard.objects.get(user=reg_user) 

        if t_type == 'Income':
            dashboard.income += t_amount
            dashboard.balance += t_amount
        else:
            dashboard.expense +=t_amount
            dashboard.balance -=t_amount
            
        dashboard.save()
        return redirect('add_transaction')
            

    

    css = 'add_transactions.css'
    context = {'css':css}
    return render(request,'add_transaction.html',context)

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')