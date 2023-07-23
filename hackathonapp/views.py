from django.contrib import auth
from django.contrib import messages

from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserCreateForm, SingUpForm,UserForm
from django.contrib.auth import views as auth_views
from .models import GC
# Create your views here.
def home(request):
    return  render(request,'index.html')

def login(request):


 # # 로그인 하고 나서 main페이지로 넘어가기
    if request.method == 'POST':
        return  render(request,'ma')
    #     userId = request.POST['username']
    #     userPw = request.POST['password']
    #     user=auth.authenticate(request, username=userId, password=userPw)
    #     if user is not None:
    #         messages.info(request,'로그인 성공 ')
    #          #로그인 성공했을때
    #         login(request,user)
    #         return render(request,'main.html')
    #     else:
    #         return render(request, 'login.html' )
    # else:
    #     # 로그인이 실패했을때
    #     form = AuthenticationForm()
    #
    # context = {
    #     'form': form,
    # }
    # return render(request, 'accounts/login.html', context)
    #     userId = request.POST['username']
    #     userPw = request.POST['password']
    #     user=auth.authenticate(request, username=userId, password=userPw)
    #     if user is not None:
    #         messages.info(request,'로그인 성공 ')
    #         auth.login(request, user)
    #         new=messages.info(request,'로그인 성공 ')
    #         return render(request,'main',new)
    #         #형식에 맞추지 않았을 때 다시 로그인 기본화면
    #     else:
    #         new=messages.info(request,'로그인 실패 ')
    #         return render(request,'login.html',new)




def main(request):

    #애는 어따 쓰는거지??
    submit_count = request.session.get('submit_count', 0)
    success = False

    row_count = GC.get_row_count()
    if row_count >= 10:
        return redirect('recommend')

    else:
        if request.method == 'POST':
            date = request.POST.get('date')
            top = request.POST.get('top')
            bottom = request.POST.get('bottom')
            vehicle = request.POST.get('vehicle')
            inout = request.POST.get('inout')
            ##??
            gc_obj = GC.objects.create(date=date, top=top, bottom=bottom, vehicle=vehicle, inout=inout)#데이터베이스 생성

            success = True
            return render(request, 'main.html', {'success':success})
        #로그인하면 이 페이지로 이동


        return  render(request,'main.html')


#signup2
def signup(request):
    # POST 요청인 경우에는 화면에서 입력한 데이터로 사용자를 생성하고 GET 요청인 경우에는 회원가입 화면을 보여준다.
    #데이터를 입력했을때
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()#입력된 데이터 저장
            return redirect('home')
        else:#형식에 맞추지 않았을 때 다시 회원가입 기본화면
            return  render(request,'signup2.html')
    #get
    else:
        form = UserForm()
    return render(request, 'signup2.html', {'form': form})
def recommend(request):
    messages.info(request,'로그인 성공 ')
    return render(request, 'recommend.html')

