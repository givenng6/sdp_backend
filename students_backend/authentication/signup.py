from rest_framework.response import Response
from rest_framework.decorators import api_view
from firebase_admin import auth
from authentication import firebase_key

@api_view(['GET'])
def myAuth(request):
    
    return Response("Path")