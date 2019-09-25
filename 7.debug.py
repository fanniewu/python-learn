import logging
#配置log输出级别
logging.basicConfig(level=logging.INFO)
'''
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
'''

def func(x):
    #assert x!=0, "x is zero"
    logging.info("----x = %d" %(x))
    return 10/x

func(0)

# assert优点：在启动程序时可以通过命令参数-O关闭assert
# logging: 不会抛出异常，可以输出到文件