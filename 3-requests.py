import time

import requests
import re

if __name__ == '__main__':
    url1 = 'http://sc.chinaz.com/tupian/shanshuifengjing.html'
    url2 = 'http://sc.chinaz.com/tupian/shanshuifengjing_%d.html'


    #with open('./pic/shanshui.html', mode='w',encoding='utf-8') as fp:
     #   fp.write(response.text)
     #   print('网页内容保存成功')

    #  <img src2="http://pic1.sc.chinaz.com/Files/pic/pic9/201907/zzpic19245_s.jpg"

    pattern = r'<img src2="(.*?)" .*?>'
    #img_urls = re.findall(pattern, response.text)

    # for img_url in img_urls:
    #     response = requests.get(img_url)
    #     content = response.content
    #     file = img_url.rsplit('/', maxsplit=1)[1]
    #     print(file)
    #     with open('./pic/%s'%(file), mode='wb') as fp:
    #         fp.write(content)
    #         print('图片%s保存成功!'%(file))
    #     time.sleep(1)

    #一共5页
    try:
        for i in range(5):
            if i == 0:
                url = url1
            else:
                url = url2%(i+1)
            response = requests.get(url=url)
            img_urls = re.findall(pattern, response.text)
            img_names = [i.rsplit('/', maxsplit=1)[1] for i in img_urls]
            print(img_names)

            for img_url, img_name in zip(img_urls, img_names):
                response = requests.get(img_url, timeout=10)
                with open('./pic/shshfj/%s'%(img_name), mode='wb') as fp:
                    fp.write(response.content)
                    print('第%d页的图片%s保存成功！'%(i+1, img_name))
                    time.sleep(1)
        # for img_url in img_urls:
        #     response = requests.get(img_url)
        #     content = response.content
        #     file = img_url.rsplit('/', maxsplit=1)[1]
        #     with open('./pic/%s' % (file), mode='wb') as fp:
        #         fp.write(content)
        #         print('图片%s保存成功!' % (file))
        #     time.sleep(1)
    except Exception as e:
        with open('./Exception.txt','a', encoding='utf-8') as fp:
            fp.write(str(e) + '/n')