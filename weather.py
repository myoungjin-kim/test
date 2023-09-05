from bs4 import BeautifulSoup as bs
import requests


def crawl_weather_data():

    html = requests.get('https://search.naver.com/search.naver?query=날씨')
    soup = bs(html.text,'html.parser')
    url = "https://search.naver.com/search.naver?query=날씨"


    # 온도 출력
    tempdata1 = soup.find('div',{'class':'temperature_text'})
    tempdata2 = tempdata1.findAll('strong')
    first_element = tempdata2[0]
    temperature = first_element.text.split()[1]
    temperature = temperature.replace('온도', '')

    #print("현재 온도 : " + temperature)

    # 습도 출력
    humidata1 = soup.find('div',{'class':'temperature_info'})
    humidata2 = humidata1.findAll('div', {'class':'sort'})
    if len(humidata2) == 4:
        second_element = humidata2[2]
        water = humidata2[1]
        water = water.text.split()[1]
        water = water.replace('강수', '')
    else:
        second_element = humidata2[1]
        water = 0
    humi = second_element.text.split()[1]
    humi = humi.replace('습도', '')

    #print("현재 습도 : " + humi)

    # 날씨 텍스트 출력
    weatdata1 = humidata1.findAll('span')
    third_element = weatdata1[2].text
    #print("현재 날씨 : " + third_element)

    # 체감온도 출력
    realtemp = humidata2[0].text.split()[1]
    realtemp = realtemp.replace('체감', '')
    #print("체감 온도 : " +  realtemp)

    # 자외선 출력
    UVdata1 = soup.find('div',{'class':'report_card_wrap'})
    UVdata2 = UVdata1.findAll('span')
    UVdata3 = UVdata2[2].text
    # print("자외선    : " + UVdata3)

    # 아이콘 출력
    weather_icon1 = soup.find('div', {'class':'weather_main'})
    weather_icon = weather_icon1.find('i')['class']
    weather_icon = ' '.join(weather_icon)

    #-----------#
    # 의상 TOP 10
    url1 = 'https://www.musinsa.com/categories/item/001001'
    response1 = requests.get(url1)
    soup1 = bs(response1.text, 'html.parser')
    tshirts1 = soup1.find_all('div', {'class':'list_img'})[:10]
    tshirts2 = 'https:'+soup1.find_all('a', attrs={'class':'img-block'})[0]['href']
    tshirts3 = soup1.find_all('a', attrs={'class':'img-block'})[0]
    tshirts4 = tshirts3.find('img')
    tshirts5 = tshirts4.get('alt')
    #print(tshirts2) # 링크
    #print(tshirts5) # 제목

    tshirts6 = soup1.find_all('p', {'class':'price'})[:10]
    tshirts7 = tshirts6[0].get_text(strip=True)
    tshirts8 = tshirts7.split('원')[1].replace(',', '') + '원'
    #print(tshirts8) # 가격

    tshirts9 = tshirts3.find('img')
    tshirts10 = tshirts9.get('data-original')
    #tshirts10 # 이미지

    return temperature, humi, realtemp, third_element, UVdata3, water, weather_icon, tshirts5, tshirts10, tshirts8, tshirts2
