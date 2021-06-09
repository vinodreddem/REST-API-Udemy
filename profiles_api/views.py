from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import models
from profiles_api import permissions
from profiles_api import serializers

class HelloViewset(viewsets.ViewSet):
    """Test API Viewset """
    serializer_class = serializers.HelloSerializer
    
    def list(self,request):
        """Return a Hello Message """
        a_viewset = [
            'Uses as an actions (list, create , retrieve, update, partial-update, destroy)',
            'Automatically maps to URLs using Routers ',
            'Provide more functionality with less code'
        ]
        
        return Response({'message':'Hello', 'a_viewset':a_viewset})
    
    def create(self, request):
        serializer = self.serializer_class(data= request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data('name')
            message = "Hello {}".format(name)
            return Response({'message':message})
                            
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
        
    
    def retrieve(self,request,pk=None):
        return Response({'http Method':'GET'})
    
    def update(self,request,pk=None):
        return Response({'http Method':'PUT'})
    
    def partial_update(self,request,pk=None):
        return Response({'http Method':'PATCH'})
    
    def destroy(self,request,pk=None):
        return Response({'http Method':'DELETE'})
        
# Create your views here.
class HelloAPIView(APIView):
    """Test API View """
    
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """ Returns a list of APIView features """
        an_apiview = ['Uses an HTTP methods as functions (get, post, put, delete)',
                      'Is similar to a traditional Django View',
                      'Gives you the most control over a application logic ',
                      'Is mapped manually to URLs']
        
        return Response({'Message':'Hello','an_apiview':an_apiview})
    
    
    def post(self, request):
        """ Create a Hello Msg with name """
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            
            return Response({'message': message})
        
        else:
            return Response(
                serializer.errors,
                status= status.HTTP_400_BAD_REQUEST            
            )
    
    def put(self, request, pk=None):
        """ Handle update an Object """
        #We will do it for specific URL function  --Primary Key generally
        return Response({'method':'PUT'})
        
    def patch(self, request, pk = None):
        """Handle a Partial Object  """
        return Response({'method':'Patch'})
    
    def delete(self, request, pk = None):
        """ Delete an Object"""
        return Response({'method':'Delete'})
    
    
class UserProfileViewset(viewsets.ModelViewSet):
    """ Handle Creating and Updating  profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile,)
    
    
    
    
    