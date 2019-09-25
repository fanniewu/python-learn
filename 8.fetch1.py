import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

"""
<a class="title-content" href="https://www.baidu.com/s?cl=3&amp;tn=baid%9D%A">世界杯八强出炉</a>
"""


def getUrl(url):
    html = getHtml(url)
    # 清洗出新的url
    #  urlre = "<a .*href=\"(https?://.*?)\".*>"
    urlre = "<a .*href=\"(https?://.*?)\".*>"
    urlList = re.findall(urlre, html)
    return urlList


def getHtml(url):
    response = requests.get(url, headers=headers).content.decode('utf-8', 'ignore')
    return response


def getInfo():
    pass

def depthCtl(url, depth):
    # 判断是否超出深度，超出就结束
    if depthDict[url] > depth:
        return
    print('\t\t\t' * depthDict[url], '抓取了第%d层，%s' % (depthDict[url], url))

    # getInfo(url)

    sonUrllist = getUrl(url)
    for newUrl in sonUrllist:
        if newUrl not in depthDict:
            depthDict[newUrl] = depthDict[url] + 1
            depthCtl(newUrl, depth)


if __name__ == '__main__':
    # 种子url
    startUrl = 'https://www.baidu.com/s?wd=世界杯'

    depthDict = {}
    depthDict[startUrl] = 1

    depthCtl(startUrl, 4)
