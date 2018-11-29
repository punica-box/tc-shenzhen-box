from django.contrib import admin

from ontofraud.models import Wallet, Transaction


class WalletAdmin(admin.ModelAdmin):
    list_display = ('hashid', 'status')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('hashid', 'from_address', 'to_address', 'amount', 'description')


admin.site.register(Wallet, WalletAdmin)
admin.site.register(Transaction, TransactionAdmin)
