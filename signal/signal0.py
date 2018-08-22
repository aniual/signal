import signal
import time


# signal.alarm(3)
# 采用默认方式
# signal.signal(signal.SIGINT, signal.SIG_DFL)
# 忽略掉信号
signal.signal(signal.SIGINT, signal.SIG_IGN)
# signal.signal(signal.SIGALRM,signal.SIG_IGN)

while True:
    time.sleep(2)
    print('ctrl+c终止')
