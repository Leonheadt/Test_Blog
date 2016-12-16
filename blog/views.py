from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Get_Test(request):

    receive = request.GET.get('value')
    print(receive)

    return HttpResponse()


