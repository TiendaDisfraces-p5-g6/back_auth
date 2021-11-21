from auth_example.models.prenda                      import Prenda
from rest_framework                                  import status,views, generics
from rest_framework.response                         import Response
from auth_example.serializers.prendaSerializer       import PrendaSerializer
from rest_framework                                  import serializers

class PrendaCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = PrendaSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
    
        return Response("prenda creada", status=status.HTTP_201_CREATED)


class PrendaListView(generics.ListAPIView):
    serializer_class = PrendaSerializer
    def get_queryset(self):
        queryset = Prenda.objects.all()
        return queryset

class PrendaUpdateView(generics.UpdateAPIView):
    serializer_class   = PrendaSerializer
    queryset           = Prenda.objects.all()

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class PrendaDeleteView(generics.DestroyAPIView):
    serializer_class   = PrendaSerializer
    queryset           = Prenda.objects.all()

    def delete(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response("prenda borrada", status=status.HTTP_204_NO_CONTENT)