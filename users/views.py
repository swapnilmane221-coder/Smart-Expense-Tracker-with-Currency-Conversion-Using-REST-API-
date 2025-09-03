from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import expense
from django.db.models import Sum
import json
from django.db.models.functions import TruncMonth




# Create your views here.
def register(request):
     if request.method=='POST':
          name=request.POST.get('name')
          username=request.POST.get('username')
          email=request.POST.get('email')
          password=str(request.POST.get('password'))
          confirm_password=str(request.POST.get('confirm-password'))
          if password!=confirm_password:
                 messages.error(request, 'Passwords do not match.')
                 return redirect('user-register')
          if len(password) < 6:
                 messages.error(request, 'Password must be at least 6 characters long.')
                 return redirect('user-login')
          User.objects.create_user(first_name=name,username=username,email=email,password=password)
          messages.success(request,'Account created successfully')
          return redirect('user-login')
     
     
     return render(request, 'register.html')

def login(request):
     if request.mathod=='POST':
          username=request.POST.get('username')
          password=request.POST.get('password')
          user=authenticate(username=username,password=password)
          if user is not None:
               login(request,user)
               return redirect('dashboard')
          else:
               messages.error(request,'Invalid username or password')
               return redirect('user-login')
     return render(request, 'login.html')

@login_required(login_url='user-login')
def dashboard(request):
     transaction_count=expense.objects.count()
     highest_category=expense.objects.values('category').annotate(total_amount=Sum('amount')).order_by('-total_amount').first()
     total_amount = expense.objects.aggregate(total_amount=Sum('amount'))['total_amount'] or 0
     category_data = expense.objects.values('category').annotate(total=Sum('amount'))
     categories = [item['category'] for item in category_data]
     amounts = [float(item['total']) for item in category_data]

     months_qs = expense.objects.annotate(month=TruncMonth('date')) \
    .values('month') \
    .annotate(total=Sum('amount')) \
    .order_by('month')     
     months = [entry['month'].strftime('%B') for entry in months_qs if entry['month']]  # Month names
     monthly_amounts = [entry['total'] for entry in months_qs]  # [800, 700, ...]
 
     context = {
        "categories": json.dumps(categories),
        "amounts": json.dumps(amounts),
        "months": json.dumps(months),
        "monthly_amounts": json.dumps(monthly_amounts),
        "transaction_count": transaction_count,
        "total_amount": total_amount,
        "high_cat": highest_category
    }
     return render(request, 'dashboard.html',context)

@login_required(login_url='user-login')
def add_expense(request):
     if request.method=='POST':
          title=request.POST.get('title')
          amount=int(request.POST.get('amount'))
          category=request.POST.get('category')
          description=request.POST.get('description')
          date=request.POST.get('date')
          print(title)
          print(amount)
          print(category)
          print(description)
          print(date)
          Expense=expense(title=title,amount=amount,category=category,description=description,date=date)
          Expense.save()
          return redirect('dashboard')
    
     return render(request, 'add-expense.html')

@login_required(login_url='user-login')
def expense_history(request):
     expense_list=expense.objects.all()
     print(expense_list)
     return render(request, 'expense-history.html',{'expense_list':expense_list})

@login_required(login_url='user-login')
def profile_setting(request):
     return render(request, 'profile-setting.html')

@login_required(login_url='user-login')
def update(request):
     expense={id:1}
     return render(request, 'update.html',{'expense':expense})