from django.shortcuts import redirect, render

from django.http import HttpResponse
from django.views.generic import TemplateView

from .forms import SessionForm

from .forms import HelloForm, FriendForm

from .models import Friend
# Create your views here.


def index6(request):
    data = Friend.objects.all()
    params = {
        'title': 'Hello',
        # 'message': 'all friends',
        # 'form': HelloForm(),
        'data': data,
    }
    # if (request.method  == 'POST'):
    #     print('a')
    #     num = request.POST['id']
    #     item = Friend.objects.get(id=num)
    #     params['data']=[item]
    #     params['form']=HelloForm(request.POST)
    # else:
    #     params['data']=Friend.objects.all()
    return render(request, 'hello/index.html', params)


def create(request):

    if(request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        # name = request.POST['name']
        # mail = request.POST['mail']
        # gender = 'gender' in request.POST
        # age = int(request.POST['age'])
        # birth = request.POST['birthday']
        # friend = Friend(name = name, mail =mail, gender = gender,\
        #                 age = age, birthday = birth)
        friend.save()
        return redirect(to='/hello')
    
    params = {
        'title':'Hello',
        'form':FriendForm(),
    }
    return render(request, 'hello/create.html', params)


# class HelloView(TemplateView):
#     # template_name = "TEMPLATE_NAME"

#     def __init__(self):
#         # print(request.keys())
#         self.params = {
#             'title': 'Hello',
#             # 'message': 'your data:',
#             'form': SessionForm(),
#             'result': None,
#         }

#     def get(self, request):
#         self.params['result'] = request.session.get('last_msg', 'No message.')
#         return render(request, 'hello/index.html', self.params)
    
#     def post(self, request):
#         # print(request.session.keys())
#         # print(request.session.items())
#         ses = request.POST['session']
#         self.params['result'] = 'send:' + ses
#         request.session['last_msg'] = ses
#         self.params['form'] = SessionForm(request.POST)
#         #セッション管理する時間を秒で指定できる。
#         request.session.set_expiry(20)
#         return render(request, 'hello/index.html', self.params)


# def index1(request):
#     if 'msg' in request.GET:
#         msg = request.GET['msg']
#         result = 'msgは、' + msg
#     else:
#         result = 'msgない'

#     return HttpResponse(result)

# def index2(request, id, nickname):
#     result = 'idは、' + str(id) + 'で、nicknameは、' + nickname
#     return HttpResponse(result)

# def index3(request):
#     params = {
#         'title':'Hello/Index',
#         'msg':'サンプルです',
#         'goto':'next',
#     }
#     return render(request, 'hello/index.html', params)

# def next(request):
#     params = {
#         'title':'Hello/Next',
#         'msg':'もう1つのページ',
#         'goto':'index3',
#     }
#     return render(request, 'hello/index.html', params)

# def index4(request):
#     params={
#         'title':'Hello/Index',
#         'msg':'お名前は？',
#     }
#     return render(request, 'hello/index.html', params)

# def form(request):
#     msg=request.POST['msg']
#     params={
#         'title':'Hello/Form',
#         'msg':'こんにちは'+msg,
#     }
#     return render(request, 'hello/index.html', params)

# def index5(request):
#     params = {
#         'title': 'Hello',
#         'message': 'your data:',
#         'form': HelloForm()
#     }
#     if(request.method == 'POST'):
#         params['message'] = '名前：' + request.POST['name']+\
#             '<br>メール:'+ request.POST['mail']+\
#             '<br>年齢：'+request.POST['age']
#         params['form'] = HelloForm(request.POST)
#     return render(request, 'hello/index.html', params)

