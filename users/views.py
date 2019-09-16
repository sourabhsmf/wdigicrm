from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import permissions

from users.models import User
from users.serializers import UserSerializer

# Create your views here.
#TODO-Convert to class based views and remove permission classes
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def user_list(request):
    """
    List all existing users.
    """
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def user_get(request , user_id):
    """
    Get a user by id
    """
    try:
            user = User.objects.get(id=user_id)
    except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def user_add(request):
    """
    Create new user
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def user_remove(request, user_id):
    """
    Delete exisiting user
    """
    try:
            user = User.objects.get(id=user_id)
    except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserSerializer(data=request.data)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def user_update(request,user_id):
    """
    Update exisiting user
    """
    try:
            user = User.objects.get(id=user_id)
    except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user , data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
