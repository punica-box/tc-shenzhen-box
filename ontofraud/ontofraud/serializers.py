from rest_framework import serializers

from ontofraud.models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('hashid', 'status')
