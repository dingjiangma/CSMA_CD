# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import time
import random

t = 0.01
#模拟的基本退避时间为0.01



def wait(wait_time):
    time.sleep(wait_time * t)


def TBE(retime):
    # 截断二进制
    retime = min(retime, 10)
    # 取重传次数与10相比较小的数
    wait_time = random.randint(0, 2 ** (retime - 1))
    # 随机选取延迟单位r
    print('退避时间:', wait_time,'t')
    wait(wait_time)


def CSMACD(retry_time):
    pass_chance = random.randint(1, 100)
    if pass_chance >70:
        print('发送成功')
        return 0
        #不冲突
    else:
        if retry_time>15:
            print('发生冲突，执行退避')
            print('重传次数达到16次,退出')
            return 1
            #重传次数达到16次
        else:
            print('发生冲突，执行退避')
            print('重传次数：',retry_time)
            TBE(retry_time)
            #执行退避操作
            return 2

def isbusy():
    channel_free = random.randint(1, 100)
    if channel_free >70:
        return 0
        #信道不忙
    else:
        return 1
        #信道忙


def main():
    ipt = input('键入s进行模拟，键入e退出\n')
    while ipt != 'e':
        retry = 1
        flag=1
        while flag==1:
            ifbusy = isbusy()
            if ifbusy==0:
                print('信道空闲，发送数据')
                csma=CSMACD(retry)
                if csma==0:
                    flag=0
                elif csma==1:
                    flag=0
                elif csma==2:
                    print('*************')
                    retry =retry+1
                    flag = 1
            elif ifbusy==1:
                print('信道忙，持续监听')
                flag =1
        ipt = input('\n键入s进行模拟，键入e退出\n')
    return 0


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
