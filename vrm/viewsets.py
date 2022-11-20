from accounts.models import User
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from vrm.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions

class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        data = User.objects.filter(id=request.user.id).values('username', 'email')[0]
        data['groups'] = request.user.groups.all().values_list('id', flat=True)
        return Response(data)