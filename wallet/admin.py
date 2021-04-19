from django.contrib import admin
from .models import Wallet, Transaction
# Register your models here.


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('wallet', 'created', 'amount', 'operation_type')


admin.site.register(Wallet)
admin.site.register(Transaction, TransactionAdmin)


