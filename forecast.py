import requests
import json
def forecast():
    from datetime import datetime, timedelta
    # 실제함수
    yesterday = (datetime.today() - timedelta(1)).strftime("%Y%m%d")  # 원하는 문자열형식으로
    # print forecast data

    here_req = requests.get("http://www.geoplugin.net/json.gp")
    # 자동으로

    if (here_req.status_code != 200):
        print("현재좌표를 불러올 수 없음")
    else:
        location = json.loads(here_req.text)
        crd = [int(float(location["geoplugin_latitude"])), int(float(location["geoplugin_longitude"]))]
        # 좌표 값을 float 값으로 설정하면 api 함수에서 오류 발생

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