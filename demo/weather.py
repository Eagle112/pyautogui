# encoding:utf-8
import requests, json
from bs4 import BeautifulSoup
#api地址

def getWeather(city):
  f = open('city.json', 'rb')
  cities = json.load(f)
  citycode = cities.get(city)
  url = 'http://www.weather.com.cn/weather/'+ citycode +'.shtml'
  response = requests.get(url)
  response.encoding ='utf-8'

  # d = response.json()
  # f = open('./response.json','w')
  # f.write(response.text)
  soup=BeautifulSoup(response.text,"lxml")
  weather_lis = soup.select('.c7d > ul li p.wea')
  # 7天的天气
  return weather_lis




# print(soup.select('.c7d > ul li p.wea')[0].string.find('雨') != -1)