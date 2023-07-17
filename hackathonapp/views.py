from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserCreateForm, SingUpForm,UserForm
from django.contrib.auth import views as auth_views
# Create your views here.
def home(request):
    return  render(request,'index.html')

def login(request):
    # 로그인 하고 나서 main페이지로 넘어가기
    return  render(request,'login.html')
def main(request):
    return  render(request,'main.html')


#signup2
def signup(request):
    # POST 요청인 경우에는 화면에서 입력한 데이터로 사용자를 생성하고 GET 요청인 경우에는 회원가입 화면을 보여준다.
    #데이터를 입력했을때
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()#입력된 데이터 저장
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            return redirect('home')
        else:#형식에 맞추지 않았을 때 다시 회원가입 기본화면
            return  render(request,'signup2.html')
    #get
    else:
        form = UserForm()
    return render(request, 'signup2.html', {'form': form})

