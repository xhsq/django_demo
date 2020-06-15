from django.shortcuts import render
from django.http import HttpResponse

def setcook(request):
    '''保存cookie'''

    response = HttpResponse('setcook')


    response.set_cookie('itcast', 'python', max_age=3600 * 24 * 14)


    return response



def getcook(request):
    '''获取cookie'''

    value = request.COOKIES.get('itcast')

    print(value)

    return  HttpResponse('getcook')
