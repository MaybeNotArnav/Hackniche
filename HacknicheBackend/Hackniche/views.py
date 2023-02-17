from django.shortcuts import render
from django.http import HttpResponse 
from rest_framework.decorators import api_view

from .chat import get_response


# Create your views here.
def test(request):
    return HttpResponse('test')


@api_view(['POST','GET'])
def chatbot(request):
    # data = request.data
    response = get_response('Hello')
    return HttpResponse(response)
