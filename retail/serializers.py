from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from retail.models import Seller, Contact


# class ContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contact
#         fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    contact_city = SerializerMethodField()

    def get_contact_city(self, instance):
        return [con.city for con in instance.seller_contact.all()]

    class Meta:
        model = Seller
        fields = '__all__'


class SellerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        exclude = ('debt',)
