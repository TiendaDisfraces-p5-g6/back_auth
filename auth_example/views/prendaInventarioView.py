from auth_example.models.prendaInventario                  import PrendaInventario
from rest_framework                                        import status,views, generics
from rest_framework.response                               import Response
from auth_example.serializers.prendaInventarioSerializer   import PrendaInventarioSerializer
from rest_framework                                        import serializers

class PrendaInventarioCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = PrendaInventarioSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
    
        return Response("prenda creada", status=status.HTTP_201_CREATED)


class PrendaInventarioListView(generics.RetrieveAPIView):
    serializer_class = PrendaInventarioSerializer
    def get_queryset(self):
        queryset = PrendaInventario.objects.all()
        return queryset

class PrendaInventarioUpdateView(generics.UpdateAPIView):
    serializer_class   = PrendaInventarioSerializer
    queryset           = PrendaInventario.objects.all()

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class PrendaInventarioDeleteView(generics.DestroyAPIView):
    serializer_class   = PrendaInventarioSerializer
    queryset           = PrendaInventario.objects.all()

    def delete(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response("prenda borrada", status=status.HTTP_204_NO_CONTENT)