import requests

if __name__ == '__main__':
    # get请求
    #url = "http://www.httpbin.org/get"
    #response = requests.get(url=url)
    #print(response.text)
    #print(response.headers)
    #url = 'http://www.httpbin.org/post'
    #response = requests.post(url, data={'name':'softpo', 'id':'pie'})
    #print(response.text)

    url = 'http://pic39.nipic.com/20140314/13212139_145949222140_2.jpg'
    response = requests.get(url)
    with open('./pic/download1.jpg', mode='wb') as fp:
        content = response.content
        fp.write(content)
        print("图片保存成功")
