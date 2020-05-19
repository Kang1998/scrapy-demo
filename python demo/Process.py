from multiprocessing import Process
import time


def test():
    while 1:
        print("test")
        time.sleep(0.5)


if __name__ == '__main__':

    p = Process(target=test)
    p.start()
    # while 1:
    #     print("main")
    #     time.sleep(1)
