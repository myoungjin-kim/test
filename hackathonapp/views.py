from django.contrib import auth

# from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, logout
# from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserCreateForm, SingUpForm,UserForm
# from django.contrib.auth import views as auth_views
from .models import GC
from forecast import forecast# 날씨정보를 저장하기위한 기상청 api
from weather import crawl_weather_data
from ai.useAI import ClothingRecommendationModel

# Create your views here.
def home(request):
     return  render(request,'index.html')



def main(request):
    success = False

    row_count = GC.get_row_count()
    if row_count >= 10:
        return redirect('recommend')

    if request.method == 'POST':
        date = request.POST.get('date')
        top = request.POST.get('top')
        bottom = request.POST.get('bottom')
        vehicle = request.POST.get('vehicle')
        inout = request.POST.get('inout')

        api_data = forecast()

        gc_obj = GC.objects.create(
            date=date,
            top=top,
            bottom=bottom,
            vehicle=vehicle,
            inout=inout,
            high=api_data['TMX'],
            low=api_data['TMN'],
            now=api_data['TMP'],
            hum=api_data['REH'],
            rain=api_data['PTY'],
            prob=api_data['pop'], # 날씨 데이터 받아오기
        )

        success = True

    return render(request, 'main.html', {'success':success})

def list(request):
    rsGC = GC.objects.all()

    return render(request, 'list.html', {
        'rsGC': rsGC
    })

def list_db(request):
    rsGC = GC.objects.all()

    values_list = []

    for item in rsGC:
        temp_list = []
        temp_list.append(item.top)
        temp_list.append(item.bottom)
        temp_list.append(item.vehicle)
        temp_list.append(item.inout)
        temp_list.append(item.high)
        temp_list.append(item.low)
        temp_list.append(item.now)
        temp_list.append(item.hum)
        temp_list.append(item.rain)
        temp_list.append(item.prob)
        values_list.append(temp_list)

    print(values_list)

    return render(request, 'list.html')



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

def extract():
    import sqlite3
    conn = sqlite3.connect('../db.sqlite3')#파일 경로를 잘 지정하자 ....
    # 커서 획득
    c = conn.cursor()
    # c.execute("SELECT * FROM auth_user")
    data=(list(c.execute("SELECT * FROM get").fetchall()))
    return data

def recommend(request):
    # 크롤링한 데이터 가져오기
    temperature, humidity, personaltemp, third_element, UVdata3, water, weather_icon, tshirts5, tshirts10, tshirts8, tshirts2 = crawl_weather_data()

    # 템플릿에 데이터 전달
    context = {
        'temperature': temperature,
        'humidity': humidity,
        'personaltemp': personaltemp,
        'third_element': third_element,
        'UVdata3':UVdata3,
        'water':water,
        'weather_icon':weather_icon,
        'tshirts5':tshirts5,
        'tshirts10':tshirts10,
        'tshirts8':tshirts8,
        'tshirts2':tshirts2,
    }
    
    #ai 사용
    if request.method == 'POST':
        vehicle = request.POST.get('vehicle')
        inout = request.POST.get('inout')
        api_data = forecast()
        
        model = ClothingRecommendationModel()
        
        extracted_data = extract() #db 데이터 가져오기
        training_data = [] #학습을 진행시킬 데이터
        #학습에 불필요한 데이터 제거 (예: 날짜)
        for item in extracted_data:
            training_data.append(item[2:])

        model.retrain_model(training_data) # 모델 학습
        input_data = [vehicle, inout, api_data['TMX'], api_data['TMN'], api_data['TMP'], api_data['REH'], api_data['PTY'], api_data['pop']]  # 예측에 사용할 데이터 입력 (리스트 형태)
        tops, bottoms = model.get_clothing_recommendation(input_data)
        
        # 예측 결과를 템플릿에 전달합니다.
        return render(request, 'recommend.html', {'tops': tops, 'bottoms': bottoms}, context)
    else:
        return render(request, 'recommend.html', context)
 
    
def re_home(request):
    success = False

    if request.method == 'POST':
        date = request.POST.get('date')
        top = request.POST.get('top')
        bottom = request.POST.get('bottom')
        vehicle = request.POST.get('vehicle')
        inout = request.POST.get('inout')

        api_data = forecast()

        gc_obj = GC.objects.create(
            date=date,
            top=top,
            bottom=bottom,
            vehicle=vehicle,
            inout=inout,
            high=api_data['TMX'],
            low=api_data['TMN'],
            now=api_data['TMP'],
            hum=api_data['REH'],
            rain=api_data['PTY'],
            prob=api_data['pop'],
        )

        success = True

    return render(request, 're_home.html', {'success': success})

def list_edit(request):
    date = request.POST.get('date')
    rsDetail = GC.objects.filter(date=date)

    return render(request, "list_edit.html", {
        'rsDetail': rsDetail
    })

def update(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        top = request.POST.get('top')
        bottom = request.POST.get('bottom')
        vehicle = request.POST.get('vehicle')
        inout = request.POST.get('inout')

    try:
        gc = GC.objects.get(date=date)
        if top != "":
            gc.top = top
        if bottom != "":
            gc.b_note = bottom
        if vehicle != "":
            gc.vehicle = vehicle
        if inout != "":
            gc.inout = inout

        # 이미 데이터베이스에 있는 값을 사용
        high = gc.high
        low = gc.low
        now = gc.now
        hum = gc.hum
        rain = gc.rain
        prob = gc.prob

        # 이미 있는 값을 업데이트
        if high is not None:
            gc.high = high
        if low is not None:
            gc.low = low
        if now is not None:
            gc.now = now
        if hum is not None:
            gc.hum = hum
        if rain is not None:
            gc.rain = rain
        if prob is not None:
            gc.prob = prob

        gc.save()
        return redirect('/list')
    except GC.DoesNotExist:
        # 원하는 날짜의 데이터가 없을 경우에 대한 처리
        pass

    return render(request, 'list_edit.html')
