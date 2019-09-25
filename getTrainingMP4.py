import time
import requests
import re

if __name__ == '__main__':
    url = "http://video.mobiletrain.org/course/index/courseId/607?pythonbdtg=01xxc=1803080169&jzl_kwd=79276527667&jzl_ctv=20650704192&jzl_mtt=1&jzl_adt=cl4&jzl_ch=11"
    response = requests.get(url)
    # with open('./training/courselist.html', mode='w', encoding='utf-8') as fp:
    #     fp.write(response.text)
    #     print("html saved")

    #<a href="javascript:;" data-url="http://7xtcwd.com1.z0.glb.clouddn.com/千锋软件测试教程：02 接口测试的意义.mp4" class="fr">点击播放</a>
    pattern = r'data-url="(.*?)"'
    videoURLs = re.findall(pattern, response.text)
    #videoURLs = videoURLs[129:175]
    print(videoURLs)
    videoNames = [i.rsplit('：', maxsplit=1)[1] for i in videoURLs]
    print(videoNames)


    try:
        for videoURL, videoName in zip(videoURLs, videoNames):
            print("%s ------ Downloading......" % (videoName))
            response = requests.get(url=videoURL, timeout=60)
            with open('./training/HP UFT/%s'%(videoName), mode='wb') as fp:
                fp.write(response.content)
                print("%s ------ Downloaded!" %(videoName))
                time.sleep(1)
    except Exception as e:
        with open('./training/Exception.txt', 'a', encoding='utf-8') as fp:
            fp.write(str(e) + '/n')


