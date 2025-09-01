from django.shortcuts import render

# Create your views here.
def register(request):
     return render(request, 'register.html')

def login(request):
     return render(request, 'login.html')

def dashboard(request):
     return render(request, 'dashboard.html')

def add_expense(request):
     return render(request, 'add-expense.html')

def expense_history(request):
     return render(request, 'expense-history.html')

def profile_setting(request):
     return render(request, 'profile-setting.html')

def update(request):
     expense={id:1}
     return render(request, 'update.html',{'expense':expense})