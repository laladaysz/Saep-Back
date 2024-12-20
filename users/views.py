# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

@api_view(['POST'])
def cadastro(request):
    nome = request.data.get('nome')
    email = request.data.get('email')

    # Verificar se os campos estão preenchidos
    if not nome or not email:
        return Response({'error': 'Nome e email são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Verificar se o email já existe
    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email já cadastrado'}, status=status.HTTP_400_BAD_REQUEST)

    # Criar o usuário
    user = User.objects.create(nome=nome, email=email)
    return Response({'nome': user.nome, 'email': user.email}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()  
    serializer = UserSerializer(users, many=True)  
    return Response(serializer.data)  


@api_view(['GET'])
def get_user_by_id(request, id):
    try:
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)
