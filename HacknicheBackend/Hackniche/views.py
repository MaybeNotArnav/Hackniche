from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response 
from rest_framework import status

from .chat import get_response
from .serializers import SiteUserSerializer,UserSerializer
from .models import SiteUser

def ment_check():
    return 
# Create your views here.
def test(request):
    return HttpResponse('test')


@api_view(['POST','GET'])
def chatbot(request):
    data = request.data
    print(data)
    if data:
        response = get_response(data['message'])
        if response == 'Mentoring mode':
            ment_check(response)
    else: response = 'Thanks' 
    return Response(response)


@api_view(['PUT'])
@parser_classes([MultiPartParser])
def profile(request,format=None):

#     {
#     "id": 3,
#     "aadhar_no": "239847",
#     "email": "test@mail.com",
#     "fname": "testname",
#     "lname": "testlname",
#     "is_mentor": false,
#     "rank": null,
#     "photo": null,
#     "user": 5
# }



    data = request.data
    user = User.objects.get(username='crappy')
    siteuser = SiteUser.objects.get(user=user)
    print(user)
    print(data)
    data['user']=user.id
    print(data)
    serializer = SiteUserSerializer(siteuser,data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register(request):
    data = request.data
    
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=data['username'])
        user.set_password(data['password'])
        user.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def login(request):
    data = request.data
    user = authenticate(email=data['email'],password=data['password'])
    if user is not None:
        login(user)