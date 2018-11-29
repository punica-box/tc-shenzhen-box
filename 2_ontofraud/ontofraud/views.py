from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView
from rest_framework import viewsets

from ontofraud.forms import WalletForm
from ontofraud.models import Wallet, Transaction
from ontofraud.serializers import WalletSerializer
from ontofraud.service import validate_wallet


class WalletViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()
    filter_fields = ('hashid', )


class MainPageView(FormView):
    template_name = 'base.html'
    form_class = WalletForm
    success_url = reverse_lazy('wallet')

    def post(self, request, *args, **kwargs):
        return redirect(reverse_lazy('wallet', args=(request.POST.get('hashid'), )))


class WalletView(DetailView):
    template_name = 'wallet.html'
    slug_field = 'hashid'
    model = Wallet
    context_object_name = 'wallet'

    def get_object(self, queryset=None):
        wallet = super(WalletView, self).get_object(queryset)
        targets = Transaction.objects.filter(to_address__status='fraud').select_related('from_address', 'to_address').all().values_list('to_address__hashid', flat=True)
        data = Transaction.objects.all().select_related('from_address', 'to_address').all().values_list('from_address__hashid', 'to_address__hashid', 'amount')
        try:
            status = validate_wallet(wallet.hashid, list(targets), list(data))
        except Exception as ex:
            print(ex)
        else:
            wallet.status = status
            wallet.save()
        return wallet

    def get_context_data(self, **kwargs):
        context = super(WalletView, self).get_context_data(**kwargs)
        context['form'] = WalletForm()
        return context
