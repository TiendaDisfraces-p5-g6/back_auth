from rest_framework                          import status, generics
from django.conf                             import settings
from rest_framework.response                 import Response
from auth_example.models.user                import User
from auth_example.serializers.userSerializer import UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)

class UserUpdateView(generics.UpdateAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.name = request.data.get("name")
        instance.phone = request.data.get("phone")
        instance.email = request.data.get("email")
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
       
