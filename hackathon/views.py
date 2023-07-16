from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserCreateForm, SingUpForm,UserForm
# Create your views here.
def home(request):
    return  render(request,'index.html')
def join(request):
    # 회윈가입하면 다시 login페이지로 보내기
    return  render(request,'join.html')
def login(request):
    # 로그인 하고 나서 main페이지로 넘어가기
    return  render(request,'login.html')
def main(request):
    return  render(request,'main.html')


#signup2
def signup(request):
    #데이터를 입력했을때
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('home')
    #get
    else:
        form = UserForm()
    return render(request, 'signup2.html', {'form': form})
# signup()
def signup_view(request):
    # GET 요청 시 HTML 응답
    if request.method == 'GET':
        form = SingUpForm
        context = {'form': form}
        return render(request, 'signup.html', context)
    else:
        # POST 요청 시 데이터 확인 후 회원 생성
        form = SingUpForm(request.POST)

        if form.is_valid():
            # 회원가입 처리
            form.save()
            return redirect('home')
        else:
            return redirect('join')

