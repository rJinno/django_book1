from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index1(request):
    if 'msg' in request.GET:
        msg = request.GET['msg']
        result = 'msgは、' + msg
    else:
        result = 'msgない'

    return HttpResponse(result)

def index2(request, id, nickname):
    result = 'idは、' + str(id) + 'で、nicknameは、' + nickname
    return HttpResponse(result)

def index3(request):
    params = {
        'title':'Hello/Index',
        'msg':'サンプルです',
        'goto':'next',
    }
    return render(request, 'hello/index.html', params)

def next(request):
    params = {
        'title':'Hello/Next',
        'msg':'もう1つのページ',
        'goto':'index3',
    }
    return render(request, 'hello/index.html', params)