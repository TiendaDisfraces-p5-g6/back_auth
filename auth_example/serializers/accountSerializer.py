from auth_example.models.account import Account
from auth_example.models.user    import User
from rest_framework              import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['prendasAlquiladas', 'fechaUltimoAlquiler']

    def to_representation(self, obj):
        account = Account.objects.get(id=obj.id)
        user = User.objects.get(id=obj.user_id)
        return {
            'id'                 : account.id,
            'prendasAlquiladas'  : account.prendasAlquiladas,
            'fechaUltimoAlquiler': account.fechaUltimoAlquiler,
            'user' : {
                'id'   : user.id,
                'name' : user.name,
                'email': user.email,
            }
        }

