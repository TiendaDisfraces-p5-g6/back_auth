from auth_example.models.prenda  import Prenda
from rest_framework              import serializers

class PrendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prenda
        fields = ['tipo_prenda', 'descripcion', 'talla', 'cantidad']

    def to_representation(self, obj):
        prenda  = Prenda.objects.get(id=obj.id)

        return {
            'id'           : prenda.id,
            'tipo_prenda'  : prenda.tipo_prenda,
            'descripcion'  : prenda.descripcion,
            'talla'        : prenda.talla,
            'cantidad'     : prenda.cantidad,
        }