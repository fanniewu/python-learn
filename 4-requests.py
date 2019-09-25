import requests
import json

    # url = "https://www.baidu.com"
    # params = {'kw':'Python学习'}
    # response = requests.get(url, params=params)
    # print(response.status_code)
    # print(response.url)

    # url = "http://apis.juhe.cn/simpleWeather/query"
    # data = {'city':'北京'}
    # response = requests.post(url, data=data)
    # with open('./weather.txt', 'w', encoding='utf-8') as fp:
    #     fp.write(response.text)


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}


def youdaoAPI(kw):
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    data = {
        "i": kw,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "1530598760913",
        "sign": "92691936d81b1aaf2316c682773c2012",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false",
    }

    response = requests.post(url, data=data, headers=headers)

    # 自带json模块
    result = response.json()
    result = result['translateResult'][0][0]['tgt']
    print(result)

if __name__ == '__main__':

        kw = input('请输入要翻译的内容：')
        youdaoAPI(kw)


