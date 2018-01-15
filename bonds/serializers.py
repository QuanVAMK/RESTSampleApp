from rest_framework import serializers
from bonds.models import Bond, Company
from django.contrib.auth.models import User

class BondSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Bond
        fields = ('url', 'id', 'issuer', 'term', 'parValue',
                  'couponRate', 'owner')

class UserSerializer(serializers.ModelSerializer):
    bonds = serializers.PrimaryKeyRelatedField(many=True,
                                               queryset=Bond.objects.all())
    companies = serializers.PrimaryKeyRelatedField(many=True,
                                               queryset=Company.objects.all())

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'bonds', 'companies')

class CompanySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Company
        fields = ('url', 'ticker', 'revenue', 'netIncome',
                  'noOfEmployees', 'owner')
