from django.contrib import admin
from .models import expense

class expenseAdmin(admin.ModelAdmin):
     list_display = ('id', 'title', 'category', 'amount', 'description', 'date')

admin.site.register(expense, expenseAdmin)
# Register your models here.
# admin.site.register(expense)

