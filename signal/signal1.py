from signal import *
import os
import time


# 信号处理函数,有固定参数格式
def handler(sig, frame):
    if sig == SIGALRM:
        print('等待闹钟')
    elif sig == SIGINT:
        print('收到了SIGINT就不结束')


alarm(7)
# 通过函数 处理信号
signal(SIGALRM, handler)
# signal(SIGINT, handler)
# 阻塞等待信号处理
pause()
# 通过while 等待
while True:
    print('waiting signal')
    time.sleep(2)
