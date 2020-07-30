from rest_framework.serializers import ModelSerializer
from .models import Contact, Phone


class PhoneSerializer(ModelSerializer):
    class Meta():
        model = Phone
        fields = '__all__'


class ContactSerializer(ModelSerializer):
    phones = PhoneSerializer(source='phone_set', many=True)

    class Meta():
        model = Contact
        fields = '__all__'
