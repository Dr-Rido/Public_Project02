from threading import Thread
from time import sleep


def dont():
    print('正在睡眠。。。')
    sleep(3)


def args_none(a=None):
    if a:
        print(a)
        print('打印完成')
    else:
        print('a不存在')


def main():
    dont()
    args_none()


if __name__ == '__main__':
    t1 = Thread(target=dont)
    t1.start()
    t2 = Thread(target=args_none)
    t2.start()

