from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'

    def create(self, validated_data):
        if 'status' not in validated_data:
            validated_data['status'] = 'Pendente'
        return super().create(validated_data)

    def update(self, instance, validated_data):
            # Remover 'id' de validated_data, para garantir que não seja alterado
            validated_data.pop('id', None)
            
            # Atualizar os campos restantes
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            
            instance.save()
            return instance