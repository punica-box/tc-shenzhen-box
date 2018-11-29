from django import forms

from ontofraud.models import Wallet


class WalletForm(forms.ModelForm):
    hashid = forms.CharField(label='Address')

    class Meta:
        model = Wallet
        fields = ('hashid', )
