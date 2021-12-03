from auth_example.models.prendaInventario     import PrendaInventario
from rest_framework                           import serializers


class PrendaInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrendaInventario
        fields = ['tipo_prenda', 'descripcion', 'talla', 'cantidad']

    def to_representation(self, obj):
        prendaInventario  = PrendaInventario.objects.get(id=obj.id)

        return {
            'id'           : prendaInventario.id,
            'tipo_prenda'  : prendaInventario.tipo_prenda,
            'descripcion'  : prendaInventario.descripcion,
            'talla'        : prendaInventario.talla,
            'cantidad'     : prendaInventario.cantidad,
        }