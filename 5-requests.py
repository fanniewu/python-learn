import requests
import json

if __name__ == '__main__':

    # url = "https://www.baidu.com"
    # params = {'kw':'Python学习'}
    # response = requests.get(url, params=params)
    # print(response.status_code)
    # print(response.url)

    url = "http://apis.juhe.cn/simpleWeather/query"
    data = {'city':'北京', 'key':'xxxx'}
    response = requests.post(url, data=data)
    with open('./weather.txt', 'w', encoding='utf-8') as fp:
        fp.write(response.text)

