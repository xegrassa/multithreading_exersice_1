import threading
import time

WORKING_TIME = 21


def task_1():
    print('Start: Thread_1: Work 2 sec')
    time.sleep(2)
    print('End  : Thread_1')


def task_2():
    print('Start: Thread_2: Work 5 sec')
    time.sleep(5)
    print('End  : Thread_2')


def time_info(start_time):
    print(int(time.time() - start_time), ' sec: ', end='')


if __name__ == '__main__':
    start_program_time = time.time()
    stop_time = start_program_time + WORKING_TIME

    thread_1 = threading.Thread(target=task_1, daemon=True)
    thread_2 = threading.Thread(target=task_2, daemon=True)
    thread_1.start()
    thread_2.start()
    stop_time_1 = None
    stop_time_2 = None
    next_start_time_1 = time.time() + WORKING_TIME
    next_start_time_2 = time.time() + WORKING_TIME

    while time.time() < stop_time:
        if not thread_1.is_alive():
            if not stop_time_1:
                stop_time_1 = time.time()
                next_start_time_1 = stop_time_1 + 5
                time_info(start_program_time)
                print('Next start time Thread_1: ', next_start_time_1 - start_program_time)
            if time.time() >= next_start_time_1:
                thread_1 = threading.Thread(target=task_1, daemon=True)
                time_info(start_program_time)

                thread_1.start()
                stop_time_1 = None

        if not thread_2.is_alive():
            if not stop_time_2:
                stop_time_2 = time.time()
                next_start_time_2 = stop_time_2 + 15
                time_info(start_program_time)
                print('Next start time Thread_2: ', next_start_time_2 - start_program_time)
            if time.time() >= next_start_time_2:
                thread_2 = threading.Thread(target=task_2, daemon=True)
                time_info(start_program_time)

                thread_2.start()
                stop_time_2 = None

    thread_1.join()
    thread_2.join()
    print('EXIT : ', str(time.time() - start_program_time))
