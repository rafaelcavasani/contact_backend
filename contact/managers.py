from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from .forms import PhoneForm


class PhoneManager(models.Manager):
    def create_all(self, phones, contact):
        for phone in phones:
            phone_form = PhoneForm(phone)
            if not phone_form.is_valid():
                return phone_form.errors
            super().get_queryset().create(contact=contact, **phone)

        return None

    def update_all(self, phones, contact):
        for phone in phones:
            phone_form = PhoneForm(phone)
            if not phone_form.is_valid():
                return phone_form.errors
            phone_id = phone.get('id', None)
            if phone_id:
                try:
                    phone_persistent = super().get_queryset().get(
                        id=phone_id, contact=contact)
                    phone_persistent.number = phone.get('number', None)
                    phone_persistent.save()
                except ObjectDoesNotExist:
                    return {'Erro ao atualizar: Telefone informado não encontrado.'}

            else:
                super().get_queryset().create(contact=contact, **phone)

        return None

    def delete_all(self, phones, contact):
        for phone in phones:
            phone_id = phone.get('id', None)
            try:
                phone_persistent = super().get_queryset().get(
                    id=phone_id, contact=contact)
                phone_persistent.delete()
            except ObjectDoesNotExist:
                return {'Erro ao excluir: Telefone informado não encontrado.'}

        return None
