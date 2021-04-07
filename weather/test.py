# encoding:utf-8
import requests, json
from bs4 import BeautifulSoup
#api地址
url = 'http://www.weather.com.cn/weather/101190401.shtml'

response = requests.get(url)
response.encoding ='utf-8'

# d = response.json()
# f = open('./response.json','w')
# f.write(response.text)
soup=BeautifulSoup(response.text,"lxml")
weather_lis = soup.select('.c7d > ul li p.wea')
for i in range(2):
  print(weather_lis[i].string)
# print(soup.select('.c7d > ul li p.wea')[0].string.find('雨') != -1)