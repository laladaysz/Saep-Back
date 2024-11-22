from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa
from .serializers import TarefaSerializer

@api_view(['POST'])
def criar_tarefa(request):
    serializer = TarefaSerializer(data=request.data)
    if serializer.is_valid():
        tarefa = serializer.save()
        return Response(TarefaSerializer(tarefa).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_tarefas(request):
    tarefas = Tarefa.objects.all()
    serializer = TarefaSerializer(tarefas, many=True)
    return Response(serializer.data)


@api_view(['PATCH'])
def update_status(request, id):
    try:
        tarefa = Tarefa.objects.get(id=id)
    except Tarefa.DoesNotExist:
        return Response({"error": "Tarefa não encontrada"}, status=status.HTTP_404_NOT_FOUND)

    # Atualizando apenas o status da tarefa
    novo_status = request.data.get("status")
    if not novo_status:
        return Response({"error": "Status é obrigatório"}, status=status.HTTP_400_BAD_REQUEST)

    tarefa.status = novo_status
    tarefa.save()

    # Serializa a tarefa atualizada
    serializer = TarefaSerializer(tarefa)
    return Response(serializer.data, status=status.HTTP_200_OK)