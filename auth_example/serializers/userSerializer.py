from auth_example.models.account import Account
from auth_example.models.user    import User
from .accountSerializer          import AccountSerializer
from rest_framework              import serializers

class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = User
        fields= ['id', 'username','password', 'name','phone', 'email', 'account']

    def create (self, validated_data):
        accountData  = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        Account.objects.create(user=userInstance, **accountData)
        return userInstance


    def to_representation(self, obj):
        user    = User.objects.get(id=obj.id)
        account = Account.objects.get(user=obj.id)
        return {
            'id'       : user.id,
            'username' : user.username,
            'password' : user.password,
            'name'     : user.name,
            'phone'    : user.phone,
            'email'    : user.email,
            'account'  :{
                'prendasAlquiladas'  : account.prendasAlquiladas,
                'fechaUltimoAlquiler': account.fechaUltimoAlquiler

            }
        }