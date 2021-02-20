import requests, xmltodict
from bs4 import BeautifulSoup
from datetime import date, timedelta
from pprint import pprint
from time import sleep
from urllib import parse
import json

def corona_summary():
    url = 'http://ncov.mohw.go.kr/'
    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'lxml')

    peoples = soup.select('.liveNumOuter ul.liveNum .num')

    results = {
        '확진환자' : int(peoples[0].text.replace(',','').replace('(누적)','')),
        '완치' : int(peoples[1].text.replace(',','')),
        '치료중' : int(peoples[2].text.replace(',','')),
        '사망' : int(peoples[3].text.replace(',',''))
    }

    return results

def corona_data():
    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson'
    serviceKey = parse.unquote('HfeTZAGkKM84MveuCGWJSh%2BjTvKSkDVwU4pM3al2sJR4ISUI%2FJy%2F%2FYfdpQdmcSLW0OEUXYosxAZBvmzNhNT6Nw%3D%3D')

    today = date.today()
    yesterday = today - timedelta(days=1)
    today = today.strftime("%Y%m%d")
    yesterday = yesterday.strftime("%Y%m%d")

    params = {
        'serviceKey' : serviceKey,
        'pageNo' : '1',
        'numOfRows' : '30',
        'startCreateDt' : yesterday,
        'endCreateDt' : today
    }

    res = requests.get(url, params=params)

    dict_data = xmltodict.parse(res.text)
    json_data = json.dumps(dict_data)
    dict_data = json.loads(json_data)

    items = dict_data['response']['body']['items']['item']

    f_string = date.today().strftime("%Y-%m-%d")

    results = []
    if f_string in items[0]['createDt']:
        for item in items:
            if f_string in item['createDt']:
                results.append(item)
    else :
        results = items

    results.reverse()
    return results