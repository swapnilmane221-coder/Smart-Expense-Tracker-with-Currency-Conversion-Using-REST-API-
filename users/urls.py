from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('user-register/', views.register, name='user-register'),
     path('login/', views.login, name='user-login'),
     path('update/<int:id>/', views.update, name='update'),
     path('profile-setting/', views.profile_setting, name='profile-setting'),
     path('dashboard/', views.dashboard, name='dashboard'),
     path('add-expense/', views.add_expense, name='add-expense'),
     path('expense-history/', views.expense_history, name='expense-history'),
     path('delete/<int:id>/', views.delete, name='delete-expense'),
]