import threading
import time

WORKING_TIME = 4


def task_1():
    print('Я задача 1 и мой интервал 5 сек и выполняюсь я 2 сек')
    time.sleep(2)


def task_2():
    print('Я задача 2 и мой интервал 15 сек и выполняюсь я 5 сек')
    time.sleep(5)


if __name__ == '__main__':
    current_time = time.time()
    stop_time = current_time + WORKING_TIME
    print('START: ', str(current_time))
    print('STOP : ', str(stop_time))

    thread_1 = threading.Thread(target=task_1)
    thread_2 = threading.Thread(target=task_2)

    while time.time() < stop_time:
        thread_1.start()
        thread_2.start()

    # thread_1.join()
    # thread_2.join()
    print('EXIT r: ', str(time.time()))
