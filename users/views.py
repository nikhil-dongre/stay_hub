from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import User
from rest_framework.exceptions import NotFound
# Create your views here.

@api_view(["GET", "POST"])
def users(request,id=None):
    if request.method == 'GET':
        if id:
            try:
                user = User.objects.get(id=id)
            except:
                raise NotFound("No such user is present ")
            serializer = UserSerializer(user)
        else:
            user = User.objects.all()
            serializer = UserSerializer(user,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        else:
            return Response(user_serializer.errors, status=400)
        
