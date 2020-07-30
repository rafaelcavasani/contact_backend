from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.db import transaction
from .models import Contact, Phone
from .serializers import ContactSerializer
from .forms import ContactForm


class ContactViewSet(ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        contact_form = ContactForm(request.data)
        if not contact_form.is_valid():
            return Response(data=contact_form.errors, status=400)

        contact = Contact.objects.create(
            name=request.data.get('name', None),
            age=request.data.get('age', None)
        )

        phones = request.data.get('phones', None)
        if phones:
            phones_add = Phone.objects.create_all(phones, contact)
            if phones_add is not None:
                transaction.set_rollback(True)
                return Response(data=phones_add, status=404)

        serializer = ContactSerializer(contact)
        return Response(data=serializer.data, status=202)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        contact_form = ContactForm(request.data)
        if not contact_form.is_valid():
            return Response(data=contact_form.errors, status=400)

        contact_id = kwargs['pk']
        try:
            contact = Contact.objects.get(id=contact_id)
        except Contact.DoesNotExist:
            data = 'Contato não encontrado.'
            return Response(data=data, status=404)

        contact.name = request.data.get('name', None)
        contact.age = request.data.get('age', None)
        contact.save()

        phones = request.data.get('phones', None)
        if phones:
            phones_update = Phone.objects.update_all(
                phones, contact)
            if phones_update is not None:
                transaction.set_rollback(True)
                return Response(data=phones_update, status=404)

        deleted_phones = request.data.get('deleted_phones', None)
        if deleted_phones:
            phones_delete = Phone.objects.delete_all(
                deleted_phones, contact)
            if phones_delete is not None:
                transaction.set_rollback(True)
                return Response(data=phones_delete, status=404)

        serializer = ContactSerializer(contact)
        return Response(data=serializer.data, status=200)
