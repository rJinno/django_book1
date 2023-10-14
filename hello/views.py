from django.shortcuts import render

from django.http import HttpResponse

from .forms import HelloForm
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

def index4(request):
    params={
        'title':'Hello/Index',
        'msg':'お名前は？',
    }
    return render(request, 'hello/index.html', params)

def form(request):
    msg=request.POST['msg']
    params={
        'title':'Hello/Form',
        'msg':'こんにちは'+msg,
    }
    return render(request, 'hello/index.html', params)

def index5(request):
    params = {
        'title': 'Hello',
        'message': 'your data:',
        'form': HelloForm()
    }
    if(request.method == 'POST'):
        params['message'] = '名前：' + request.POST['name']+\
            '<br>メール:'+ request.POST['mail']+\
            '<br>年齢：'+request.POST['age']
        params['form'] = HelloForm(request.POST)
    return render(request, 'hello/index.html', params)

