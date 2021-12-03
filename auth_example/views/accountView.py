from rest_framework                             import status, views,generics
from django.conf                                import settings
from rest_framework.response                    import Response
from auth_example.models.account                import Account
from auth_example.serializers.accountSerializer import AccountSerializer

class AccountCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
    
        return Response("cuenta creada", status=status.HTTP_201_CREATED)

class ListAccountsView(generics.RetrieveAPIView):
    queryset         = Account.objects.all()
    serializer_class = AccountSerializer
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)

  