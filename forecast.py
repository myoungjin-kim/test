import requests
import json
import math

NX = 149            ## X축 격자점 수
NY = 253            ## Y축 격자점 수

Re = 6371.00877     ##  지도반경
grid = 5.0          ##  격자간격 (km)
slat1 = 30.0        ##  표준위도 1
slat2 = 60.0        ##  표준위도 2
olon = 126.0        ##  기준점 경도
olat = 38.0         ##  기준점 위도
xo = 210 / grid     ##  기준점 X좌표
yo = 675 / grid     ##  기준점 Y좌표
first = 0

if first == 0 :
    PI = math.asin(1.0) * 2.0
    DEGRAD = PI/ 180.0
    RADDEG = 180.0 / PI


    re = Re / grid
    slat1 = slat1 * DEGRAD
    slat2 = slat2 * DEGRAD
    olon = olon * DEGRAD
    olat = olat * DEGRAD

    sn = math.tan(PI * 0.25 + slat2 * 0.5) / math.tan(PI * 0.25 + slat1 * 0.5)
    sn = math.log(math.cos(slat1) / math.cos(slat2)) / math.log(sn)
    sf = math.tan(PI * 0.25 + slat1 * 0.5)
    sf = math.pow(sf, sn) * math.cos(slat1) / sn
    ro = math.tan(PI * 0.25 + olat * 0.5)
    ro = re * sf / math.pow(ro, sn)
    first = 1

def mapToGrid(lat, lon, code = 0 ):
    ra = math.tan(PI * 0.25 + lat * DEGRAD * 0.5)
    ra = re * sf / pow(ra, sn)
    theta = lon * DEGRAD - olon
    if theta > PI :
        theta -= 2.0 * PI
    if theta < -PI :
        theta += 2.0 * PI
    theta *= sn
    x = (ra * math.sin(theta)) + xo
    y = (ro - ra * math.cos(theta)) + yo
    x = int(x + 1.5)
    y = int(y + 1.5)
    return x, y

def forecast():
    from datetime import datetime, timedelta
    # 실제함수
    yesterday = (datetime.today() - timedelta(1)).strftime("%Y%m%d")  # 원하는 문자열형식으로
    # print forecast data

    here_req = requests.get("http://www.geoplugin.net/json.gp")
    # 자동으로

    location = json.loads(here_req.text)
    lat, lon = [float(location["geoplugin_latitude"]), float(location["geoplugin_longitude"])]

    crd = mapToGrid(lat, lon)

    # def forecast():
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
    key = 'TwoMG6Z71zy+QFydVUxVupQLdYSXX/1qg63Da6n4bf4z69mofJAZCe3byVt2j66m/CFRtqizSwYDG7obG/Y5FQ=='
    todaydate = datetime.today().strftime("%Y%m%d")  # 오늘 날짜를 불러오기위한 함수
    params = {
        'serviceKey': key,
        'pageNo': '1',
        'numOfRows': '1000',
        'dataType': 'JSON',
        'base_date': yesterday,
        'base_time': '2300',  # 그전날11시 기준예보으로
        'nx': crd[0],
        'ny': crd[1]
    }

    # 수정한다 
    response = requests.get(url, params=params)

    json_data = response.json()
    RAIN = []
    forecastdata = {}
    # 예측날짜는오늘로
    for item in json_data['response']['body']['items']['item']:
        # 일 최고온도 하나씩
        if item['fcstDate'] == todaydate and item["category"] == "TMX":
            forecastdata["TMX"] = float(item['fcstValue'])
        # 일 최저온도 하나씩
        if item['fcstDate'] == todaydate and item["category"] == "TMN":
            forecastdata["TMN"] = float(item['fcstValue'])  # 현재온도 시간별
        if item['fcstDate'] == todaydate and item["category"] == "TMP" and item['fcstTime'] == '0800':
            forecastdata["TMP"] = float(item['fcstValue'])

        #     습도 시간별
        if item['fcstDate'] == todaydate and item["category"] == "REH" and item['fcstTime'] == '1100':
            forecastdata["REH"] = float(item['fcstValue'])
        #     강수형태 시간별 pty
        if item['fcstDate'] == todaydate and item["category"] == "PTY" and item['fcstTime'] == '1100':
            forecastdata["PTY"] = float(item['fcstValue'])
        #     강수확률 60 넘는게 있으면 비온다 1 비 안온다0 prob
        if item['fcstDate'] == todaydate and item["category"] == "POP":
            if int(item['fcstValue']) >= 60:  # 반복문 돌면서 비가 오는 시간대를 전부체크
                RAIN.append(1)  #
    # 비오는시간이 6시간이상이면  비온다 1 비 안온다0
    if RAIN.count(1) >= 6:
        forecastdata['pop'] = 1
    else:
        forecastdata['pop'] = 0
    #         print((item["fcstValue"]))<class 'str'>
    return forecastdata