import threading
import time
from my_logging import configure_logger
import logging

WORKING_TIME = 21


def task_1():
    logger.info('Start Thread_1: Work 2 sec')
    time.sleep(2)
    logger.info('End   Thread_1')


def task_2():
    logger.info('Start Thread_2: Work 5 sec')
    time.sleep(5)
    logger.info('End   Thread_2')


def run_thread(task, thread_name: str = 'Thread-1', interval: int = 5):
    for thread in threading.enumerate():
        if thread_name in thread.name:
            return None

    stop_time = None
    next_start_time = time.time() + WORKING_TIME
    if not thread.is_alive():
        if not stop_time:
            stop_time = time.time()
            next_start_time = stop_time + interval
        if time.time() >= next_start_time:
            thread = threading.Thread(target=task, name=thread_name, daemon=True)
            thread.start()
            stop_time = None


if __name__ == '__main__':
    configure_logger()
    logger = logging.getLogger()

    start_program_time = time.time()
    stop_time = start_program_time + WORKING_TIME
    logger.info(f'Время работы программы: {WORKING_TIME} sec')

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
            if time.time() >= next_start_time_1:
                thread_1 = threading.Thread(target=task_1, daemon=True)
                thread_1.start()
                stop_time_1 = None

        if not thread_2.is_alive():
            if not stop_time_2:
                stop_time_2 = time.time()
                next_start_time_2 = stop_time_2 + 15
            if time.time() >= next_start_time_2:
                thread_2 = threading.Thread(target=task_2, daemon=True)
                thread_2.start()
                stop_time_2 = None

    thread_1.join()
    thread_2.join()
