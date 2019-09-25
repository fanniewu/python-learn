#urllib是python自带的网络连接库
import urllib.request
import gzip

#这是python语言的主入口
if __name__ == '__main__':
    #url是要爬取的网址
    #url = "http://www.baidu.com"
    url = "http://www.qq.com"
    #response是特定网址返回的数据
    response = urllib.request.urlopen(url)
    #发起请求，百度服务器就会响应，响应头
    #getcode获取响应码，200是成功
    #返回的所有数据都在response中，包括网页内容
    #print(response.info())
    #print(response.getcode())
    #print(type(response))
    #b'--->输出的是字节
    #print(response.read().decode('utf-8'))

    #使用gzip进行解压缩，然后数据就可以获取了
    b = response.read()
    data = gzip.decompress(b)
    print(data.decode('gbk'))


