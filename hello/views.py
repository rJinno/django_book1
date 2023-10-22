from django.shortcuts import redirect, render

from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Count, Sum, Avg, Min, Max
from django.core.paginator import Paginator

from .forms import SessionForm

from .forms import HelloForm, FriendForm, FindForm, MessageForm

from .models import Friend, Message
# Create your views here.


def index6(request, num=1):
    data = Friend.objects.all()
    page = Paginator(data, 3)
    # re1 = Friend.objects.aggregate(Count('age'))
    # re2 = Friend.objects.aggregate(Sum('age'))
    # msg = str(re1['age__count']) + ' | ' + str(re2['age__sum'])
    params = {
        'title': 'Hello',
        'message': '',
        # 'form': HelloForm(),
        'data': page.get_page(num),
    }

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

def edit(request, num):
    obj = Friend.objects.get(id=num)
    if(request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id': num,
        'form': FriendForm(instance=obj),
    }
    return render(request, 'hello/edit.html', params)

def delete(request, num):
    friend = Friend.objects.get(id = num)
    if(request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id': num,
        'obj': friend,
    }
    return render(request, 'hello/delete.html', params)

class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend

def find(request):
    if(request.method == 'POST'):
        form = FindForm(request.POST)
        find = request.POST['find']
        data = Friend.objects.filter(name__startswith=find)
        msg = 'Results: ' + str(data.count())
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'message': msg,
        'form': form,
        'data': data,
    }
    return render(request, 'hello/find.html', params)

def message(request, page=1):
    if(request.method == 'POST'):
        obj = Message()
        form = MessageForm(request.POST, instance=obj)
        form.save()
    data = Message.objects.all().reverse()
    paginator = Paginator(data, 2)
    params = {
        'title': 'Message',
        'form': MessageForm(),
        'data': paginator.get_page(page),
    }
    return render(request, 'hello/message.html', params)
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

