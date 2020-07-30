from rest_framework.viewsets import ViewSet
from .models import Contact
from .serializers import ContactSerializer


class ContactViewSet(ViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
