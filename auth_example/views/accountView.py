from rest_framework                          import status, generics
from django.conf                             import settings
from auth_example.models.account             import Account
from auth_example.serializers.userSerializer import AccountSerializer

class ListAccountsView(generics.RetrieveAPIView):
    queryset         = Account.objects.all()
    serializer_class = AccountSerializer
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)

  