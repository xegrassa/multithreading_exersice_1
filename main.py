import logging
import time
from threading import Thread, Event

from my_logging import configure_logger

WORKING_TIME = 21


def task_1(done_event: Event):
    logger.info('Start Thread_1: Work 2 sec')
    time.sleep(2)
    logger.info('End   Thread_1')
    done_event.set()


def task_2(done_event: Event):
    logger.info('Start Thread_2: Work 5 sec')
    time.sleep(5)
    logger.info('End   Thread_2')
    done_event.set()


class Watcher:
    """
    :atribute task - задача которую надо делать
    :atribute interval - интервал между задачами
    :atribute start_time - время когда начать следующий поток после ожидания интервала
    :atribute thread_end - Event что поток законч работу
    """

    def __init__(self, task, interval: int):
        self.task = task
        self.interval = interval
        self.thread_end = Event()
        self.start_time = time.time()

    def runner(self) -> None:
        """
        Создание и запуск потока.
        Ставится флаг что требуется поставить время запуска потока
        """
        if self.is_done():
            self.set_start_time()
            self.thread_end.clear()
        if self.is_ready():
            Thread(target=self.task, args=(self.thread_end,), daemon=True).start()
            self.start_time = 0

    def set_start_time(self) -> None:
        """
        Установка времени когда запустить снова поток.
        """
        self.start_time = time.time() + self.interval

    def is_ready(self) -> bool:
        """
        Проверка что поток можно запускать
        """
        if (time.time() >= self.start_time and self.start_time != 0):
            return True
        return False

    def is_done(self) -> bool:
        """
        Проверка что поток закончил работу
        """
        return self.thread_end.is_set()


if __name__ == '__main__':
    configure_logger()
    logger = logging.getLogger()
    logger.info(f'Время работы программы: {WORKING_TIME} sec')

    start_program_time = time.time()
    stop_time = start_program_time + WORKING_TIME
    watch_1 = Watcher(task=task_1, interval=5)
    watch_2 = Watcher(task=task_2, interval=10)
    while time.time() < stop_time:
        watch_1.runner()
        watch_2.runner()
