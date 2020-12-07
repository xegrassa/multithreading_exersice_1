import logging
import time
from threading import Thread

from my_logging import configure_logger

WORKING_TIME = 21


def task_1():
    logger.info('Start Thread_1: Work 2 sec')
    time.sleep(2)
    logger.info('End   Thread_1')


def task_2():
    logger.info('Start Thread_2: Work 5 sec')
    time.sleep(5)
    logger.info('End   Thread_2')


class Watcher:
    """
    :atribute task - задача которую надо делать
    :atribute interval - интервал между задачами
    :atribute thread - поток который делает задачу
    :atribute start_time - время когда начать следующий поток после ожидания интервала
    :atribute need_interval - требуется ли выставить время следующего потока
    """
    task = None
    interval: int = None
    thread: Thread = Thread(target=task)
    start_time = 0
    need_interval: bool = False

    def __init__(self, task, interval):
        self.task = task
        self.interval = interval

    def runner(self) -> None:
        """
        Создание и запуск потока.
        Ставится флаг что требуется поставить время запуска потока
        """
        self.thread = Thread(target=self.task)
        self.thread.start()
        self.need_interval = True

    def set_start_time(self) -> None:
        """
        Установка времени когда запустить снова поток.
        Флаг что надо поставить время запуска убирается
        """
        if self.need_interval and not self.is_alive():
            self.start_time = time.time() + self.interval
            self.need_interval = False

    def is_ready(self) -> bool:
        """
        Проверка что поток можно запускать
        Потока нет - Время запуска подошло - Время запуска установлено
        """
        self.set_start_time()
        if not self.is_alive() and self.is_interval_done() and not self.need_interval:
            return True
        return False

    def is_alive(self) -> bool:
        """
        Проверка что поток жив
        """
        return self.thread.is_alive()

    def is_interval_done(self) -> bool:
        """
        Проверка что время запуска подошло
        """
        if time.time() >= self.start_time:
            return True
        return False


if __name__ == '__main__':
    configure_logger()
    logger = logging.getLogger()
    logger.info(f'Время работы программы: {WORKING_TIME} sec')

    start_program_time = time.time()
    stop_time = start_program_time + WORKING_TIME
    watch_1 = Watcher(task=task_1, interval=5)
    watch_2 = Watcher(task=task_2, interval=10)
    while time.time() < stop_time:
        if watch_1.is_ready():
            watch_1.runner()
        if watch_2.is_ready():
            watch_2.runner()
